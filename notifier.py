#!/usr/bin/env python3
"""AI RAN Watcher — Slack notifier (digest.md push時に実行)"""

from __future__ import annotations

import os
import re
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import quote

BASE_DIR = Path(__file__).parent
DIGEST_FILE = BASE_DIR / "digest.md"
JST = timezone(timedelta(hours=9))


# ── digest.md パーサー ────────────────────────────────────────────────────────

def parse_digest(content: str) -> dict:
    """digest.md を解析して記事リストと見出し情報を返す"""
    date_m = re.search(r"# 📡 AI RAN Digest — (\S+)", content)
    date   = date_m.group(1) if date_m else datetime.now(JST).strftime("%Y-%m-%d")

    count_m = re.search(r"新規記事: (\d+)件", content)
    count   = int(count_m.group(1)) if count_m else 0

    cat_m    = re.search(r"(🔴標準化:\d+[^\n]+)", content)
    cat_line = cat_m.group(1) if cat_m else ""

    articles = []
    lines = content.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"([🔺・]) \*\*(.+?)\*\*", lines[i])
        if m:
            priority = "high" if m.group(1) == "🔺" else "medium"
            title    = m.group(2)
            url = source = ""
            bullets: list[str] = []

            if i + 1 < len(lines):
                parts = lines[i + 1].strip().split(" | ")
                source = parts[0].strip() if len(parts) >= 2 else ""
                url    = parts[-1].strip()

            j = i + 2
            while j < len(lines) and lines[j].strip():
                bl = lines[j].strip()
                if bl.startswith("•"):
                    bullets.append(bl)
                j += 1

            articles.append({"title": title, "url": url,
                              "source": source, "priority": priority,
                              "bullets": bullets})
            i = j
        else:
            i += 1

    return {"date": date, "count": count, "cat_line": cat_line, "articles": articles}


# ── Slack Bot API ─────────────────────────────────────────────────────────────

def slack_post(text: str, bot_token: str, channel_id: str,
               thread_ts: str = "") -> str:
    payload: dict = {"channel": channel_id, "text": text, "mrkdwn": True}
    if thread_ts:
        payload["thread_ts"] = thread_ts
    try:
        resp = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={"Authorization": f"Bearer {bot_token}",
                     "Content-Type": "application/json"},
            json=payload, timeout=10,
        )
        data = resp.json()
        if data.get("ok"):
            ts = data.get("ts", "")
            print(f"  Slack 投稿({'スレッド' if thread_ts else 'メイン'}): ts={ts}")
            return ts
        print(f"  Slack エラー: {data.get('error')}")
        return ""
    except Exception as e:
        print(f"  Slack 送信エラー: {e}")
        return ""


# ── Claude 深掘りリンク ───────────────────────────────────────────────────────

def make_claude_link(article_url: str) -> str:
    """記事URLを渡すとClaudeで深掘りするためのURLを返す"""
    prompt = f"次の記事についてAI RANの観点から内容を深掘りしてください: {article_url}"
    return f"https://claude.ai/new?q={quote(prompt)}"


# ── 通知 ──────────────────────────────────────────────────────────────────────

def notify(digest: dict, bot_token: str, channel_id: str):
    top = digest["articles"][:10]

    top_lines = "\n".join(
        f"{'🔺' if a['priority'] == 'high' else '・'} "
        f"<{a['url']}|{a['title'][:70]}> _{a['source']}_"
        for a in top
    ) if top else "本日の新規記事はありません"

    claude_url   = os.environ.get("CLAUDE_PROJECT_URL", "")
    project_link = f"\n📖 <{claude_url}|Coworkで全件確認>" if claude_url else ""

    main_text = (
        f"<!here> 📡 *AI RAN Daily — {digest['date']}*\n"
        f"新規記事: *{digest['count']}件*\n"
        f"{digest['cat_line']}\n"
        f"\n*トップ{len(top)}件*\n"
        f"{top_lines}"
        f"{project_link}"
    )

    thread_ts = slack_post(main_text, bot_token, channel_id)
    if not thread_ts or not top:
        return

    for a in top:
        article_text = (
            f"{'🔺' if a['priority'] == 'high' else '・'} "
            f"*{a['title'][:80]}*\n"
            f"<{a['url']}|{a['source']}>\n"
        )
        if a["bullets"]:
            article_text += "\n" + "\n".join(a["bullets"])
        # Claude 深掘りリンク
        article_text += f"\n🤖 <{make_claude_link(a['url'])}|Claudeで深掘り>"
        slack_post(article_text, bot_token, channel_id, thread_ts)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if not DIGEST_FILE.exists():
        print("digest.md が見つかりません")
        return

    content = DIGEST_FILE.read_text(encoding="utf-8")
    digest  = parse_digest(content)
    print(f"digest.md 解析: {digest['count']}件, {len(digest['articles'])}記事")

    bot_token  = os.environ.get("SLACK_BOT_TOKEN", "")
    channel_id = os.environ.get("SLACK_CHANNEL_ID", "")

    if bot_token and channel_id:
        notify(digest, bot_token, channel_id)
    else:
        print("Slack: SLACK_BOT_TOKEN または SLACK_CHANNEL_ID 未設定のためスキップ")


if __name__ == "__main__":
    main()
