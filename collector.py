#!/usr/bin/env python3
"""AI RAN Watcher — daily article collector"""

from __future__ import annotations

import feedparser
import requests
from bs4 import BeautifulSoup
import yaml
import json
import re
import os
import hashlib
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urljoin

BASE_DIR = Path(__file__).parent
SOURCES_FILE = BASE_DIR / "sources.yaml"
KEYWORDS_FILE = BASE_DIR / "keywords.yaml"
SEEN_URLS_FILE = BASE_DIR / "seen_urls.json"
DIGEST_FILE = BASE_DIR / "digest.md"

JST = timezone(timedelta(hours=9))
DEDUP_DAYS = 30
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AI-RAN-Watcher/1.0)"}

# IEEEのTOCに含まれるメタエントリを除外するキーワード
_NOISE_TITLES = {
    "front cover", "back cover", "cover 2", "cover 3", "table of contents",
    "ieee comsoc", "comsoc training", "comsoc membership", "board of governors",
    "editor-in-chief", "author index", "publication information",
    "erratum", "announcement",
}


# ── Config ────────────────────────────────────────────────────────────────────

def load_config():
    with open(SOURCES_FILE) as f:
        sources = yaml.safe_load(f)
    with open(KEYWORDS_FILE) as f:
        keywords = yaml.safe_load(f)
    return sources["sources"], keywords


def load_seen_urls() -> dict:
    if SEEN_URLS_FILE.exists():
        with open(SEEN_URLS_FILE) as f:
            return json.load(f)
    return {}


def save_seen_urls(seen: dict):
    cutoff = (datetime.now(JST) - timedelta(days=DEDUP_DAYS)).strftime("%Y-%m-%d")
    cleaned = {k: v for k, v in seen.items() if v >= cutoff}
    with open(SEEN_URLS_FILE, "w") as f:
        json.dump(cleaned, f, indent=2)


def url_hash(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:12]


# ── Fetchers ──────────────────────────────────────────────────────────────────

def fetch_rss(source: dict) -> list[dict]:
    try:
        feed = feedparser.parse(source["url"])
        articles = []
        for entry in feed.entries[:50]:
            title = re.sub(r"<[^>]+>", "", entry.get("title", "")).strip()
            if title.lower() in _NOISE_TITLES:
                continue
            articles.append({
                "title": title,
                "url": entry.get("link", ""),
                "summary": re.sub(r"<[^>]+>", "", entry.get("summary", "")),
                "source_name": source["name"],
                "category": source["category"],
                "priority": source["priority"],
            })
        print(f"  [{len(articles):>2}件] {source['name']}")
        return articles
    except Exception as e:
        print(f"  [ERROR] {source['name']}: {e}")
        return []


def fetch_scrape(source: dict) -> list[dict]:
    try:
        resp = requests.get(source["url"], headers=HEADERS, timeout=20)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        cfg = source.get("scrape_config", {})
        articles = []

        if cfg.get("article_selector"):
            items = soup.select(cfg["article_selector"])[:25]
            for item in items:
                a_tag = item.select_one(cfg.get("link_selector", "a"))
                title_tag = item.select_one(cfg.get("title_selector", "h2,h3,a"))
                if not a_tag:
                    continue
                url = urljoin(source["url"], a_tag.get("href", ""))
                if not url.startswith("http"):
                    continue
                title = (title_tag.get_text(strip=True) if title_tag else a_tag.get_text(strip=True))
                if len(title) < 10:
                    continue
                articles.append({
                    "title": title,
                    "url": url,
                    "summary": "",
                    "source_name": source["name"],
                    "category": source["category"],
                    "priority": source["priority"],
                })
        else:
            # generic fallback
            for a in soup.find_all("a", href=True):
                text = a.get_text(strip=True)
                if not (20 <= len(text) <= 200):
                    continue
                url = urljoin(source["url"], a["href"])
                if not url.startswith("http") or url == source["url"]:
                    continue
                articles.append({
                    "title": text,
                    "url": url,
                    "summary": "",
                    "source_name": source["name"],
                    "category": source["category"],
                    "priority": source["priority"],
                })

        print(f"  [{len(articles):>2}件] {source['name']}")
        return articles
    except Exception as e:
        print(f"  [ERROR] {source['name']}: {e}")
        return []


# ── Filter & Score ────────────────────────────────────────────────────────────

def matches_any(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    for kw in keywords:
        kw_lower = kw.lower()
        # 4文字以下は単語境界マッチで誤検知を防ぐ
        if len(kw) <= 4:
            if re.search(r"\b" + re.escape(kw_lower) + r"\b", text_lower):
                return True
        else:
            if kw_lower in text_lower:
                return True
    return False


def score(article: dict) -> int:
    s = {"high": 10, "medium": 5, "low": 1}.get(article["priority"], 0)
    s += {"standardization": 5, "paper": 3, "corporate": 4, "media_jp": 2, "media": 0}.get(article["category"], 0)
    return s


# ── Digest ────────────────────────────────────────────────────────────────────

SECTION_MAP = [
    ("standardization", "## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）"),
    ("paper",           "## 📄 論文・技術文書（IEEE Xplore等）"),
    ("corporate",       "## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank）"),
    ("media_jp",        "## 🇯🇵 日本語メディア"),
    ("media",           "## 📰 業界・一般メディア（英語）"),
]


def generate_digest(articles: list[dict]) -> str:
    now = datetime.now(JST)
    by_cat: dict[str, list] = {cat: [] for cat, _ in SECTION_MAP}
    for a in articles:
        by_cat.setdefault(a["category"], []).append(a)

    lines = [
        f"# 📡 AI RAN Digest — {now.strftime('%Y-%m-%d')}",
        "",
        f"収集日時: {now.strftime('%Y-%m-%d %H:%M')} JST | 新規記事: {len(articles)}件",
        "",
    ]

    for cat, heading in SECTION_MAP:
        items = sorted(by_cat.get(cat, []), key=score, reverse=True)
        if not items:
            continue
        lines += [heading, ""]
        for a in items:
            mark = "🔺" if a["priority"] == "high" else "・"
            lines.append(f"{mark} **{a['title']}**")
            lines.append(f"   {a['source_name']} | {a['url']}")
            if a.get("summary"):
                lines.append(f"   {a['summary'][:160]}")
            lines.append("")

    return "\n".join(lines)


# ── Slack Bot API ─────────────────────────────────────────────────────────────

def slack_post(text: str, bot_token: str, channel_id: str, thread_ts: str = "") -> str:
    """chat.postMessage でメッセージを投稿。成功時は ts を返す"""
    payload: dict = {"channel": channel_id, "text": text, "mrkdwn": True}
    if thread_ts:
        payload["thread_ts"] = thread_ts
    try:
        resp = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={
                "Authorization": f"Bearer {bot_token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10,
        )
        data = resp.json()
        if data.get("ok"):
            ts = data.get("ts", "")
            label = "スレッド" if thread_ts else "メイン"
            print(f"  Slack 投稿({label}): ts={ts}")
            return ts
        else:
            print(f"  Slack エラー: {data.get('error')}")
            return ""
    except Exception as e:
        print(f"  Slack 送信エラー: {e}")
        return ""


# ── GitHub Models 日本語要約 ───────────────────────────────────────────────────

def summarize_articles(articles: list[dict], github_token: str) -> dict:
    """GitHub Models (gpt-4o-mini) でトップ記事の日本語箇条書き要約を生成"""
    if not articles or not github_token:
        return {}

    articles_text = "\n\n".join(
        f"[記事{i + 1}]\nタイトル: {a['title']}"
        + (f"\n概要(英語): {a['summary'][:300]}" if a.get("summary") else "")
        for i, a in enumerate(articles)
    )

    prompt = (
        "以下のAI RAN関連記事を日本語の箇条書きでサマリーしてください。\n\n"
        "ルール:\n"
        "- 各記事2〜4個の箇条書き\n"
        "- 合計100〜200字程度（記事の内容量に応じて柔軟に調整）\n"
        "- 第一種陸上特殊無線技士レベルの読者を想定、専門用語はそのまま使用\n"
        "- 出力フォーマットを厳守すること\n\n"
        f"{articles_text}\n\n"
        "出力フォーマット（このまま出力）:\n"
        "[記事1]\n• 要点\n• 要点\n\n[記事2]\n• 要点\n• 要点"
    )

    try:
        resp = requests.post(
            "https://models.inference.ai.azure.com/chat/completions",
            headers={
                "Authorization": f"Bearer {github_token}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 2000,
                "temperature": 0.3,
            },
            timeout=30,
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        print(f"  GitHub Models 要約生成: {len(articles)}件")
        return _parse_summaries(content)
    except Exception as e:
        print(f"  GitHub Models エラー（要約なしで続行）: {e}")
        return {}


def _parse_summaries(content: str) -> dict:
    """[記事N] ブロックを {index: bullets_str} にパース"""
    summaries: dict = {}
    current_idx = None
    current_bullets: list = []

    for line in content.split("\n"):
        line = line.strip()
        m = re.match(r"\[記事(\d+)\]", line)
        if m:
            if current_idx is not None and current_bullets:
                summaries[current_idx] = "\n".join(current_bullets)
            current_idx = int(m.group(1)) - 1
            current_bullets = []
        elif line.startswith("•") and current_idx is not None:
            current_bullets.append(line)

    if current_idx is not None and current_bullets:
        summaries[current_idx] = "\n".join(current_bullets)

    return summaries


# ── Slack 通知オーケストレーター ───────────────────────────────────────────────

def notify_slack(new_articles: list[dict], alert_articles: list[dict],
                 bot_token: str, channel_id: str, github_token: str):
    now = datetime.now(JST).strftime("%Y-%m-%d")

    # カテゴリ別件数
    cat_counts: dict[str, int] = {}
    for a in new_articles:
        cat_counts[a["category"]] = cat_counts.get(a["category"], 0) + 1

    cat_line = "　".join([
        f"🔴標準化:{cat_counts.get('standardization', 0)}",
        f"📄論文:{cat_counts.get('paper', 0)}",
        f"🏢企業:{cat_counts.get('corporate', 0)}",
        f"🇯🇵国内:{cat_counts.get('media_jp', 0)}",
        f"📰海外:{cat_counts.get('media', 0)}",
    ])

    top = sorted(new_articles, key=score, reverse=True)[:5]
    top_lines = "\n".join(
        f"{'🔺' if a['priority'] == 'high' else '・'} "
        f"<{a['url']}|{a['title'][:70]}> _{a['source_name']}_"
        for a in top
    ) if top else "　本日の新規記事はありません"

    alert_text = f"🚨 *アラート {len(alert_articles)}件あり*" if alert_articles else "アラート: なし"
    claude_url = os.environ.get("CLAUDE_PROJECT_URL", "")
    project_link = f"\n📖 <{claude_url}|Claude Projectで全件確認>" if claude_url else ""

    # ① メインメッセージ投稿 → thread_ts 取得
    main_text = (
        f"<!here> 📡 *AI RAN Daily — {now}*\n"
        f"新規記事: *{len(new_articles)}件*\n"
        f"{cat_line}\n"
        f"\n*トップ{len(top)}件*\n"
        f"{top_lines}\n"
        f"\n{alert_text}{project_link}"
    )
    thread_ts = slack_post(main_text, bot_token, channel_id)
    if not thread_ts or not top:
        return

    # ② アラート記事をスレッドの先頭に投稿
    if alert_articles:
        alert_lines = "\n".join(
            f"• <{a['url']}|{a['title']}> ({a['source_name']})"
            for a in alert_articles[:5]
        )
        slack_post(
            f"🚨 *アラート記事*\n{alert_lines}",
            bot_token, channel_id, thread_ts,
        )

    # ③ GitHub Models で日本語要約を一括生成
    summaries = summarize_articles(top, github_token)

    # ④ 記事ごとにスレッドへ投稿
    for i, a in enumerate(top):
        article_text = (
            f"{'🔺' if a['priority'] == 'high' else '・'} "
            f"*{a['title'][:80]}*\n"
            f"<{a['url']}|{a['source_name']}>\n"
        )
        summary = summaries.get(i, "")
        if summary:
            article_text += f"\n{summary}"
        slack_post(article_text, bot_token, channel_id, thread_ts)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    sources, keywords = load_config()
    filter_kws = keywords["filter_keywords"]
    alert_kws = keywords["alert_keywords"]
    seen = load_seen_urls()

    print("=== 収集開始 ===")
    raw: list[dict] = []
    for source in sources:
        if not source.get("enabled", True):
            continue
        raw += fetch_rss(source) if source["type"] == "rss" else fetch_scrape(source)

    print(f"\n取得合計: {len(raw)}件")

    # keyword filter
    filtered = [a for a in raw if matches_any(f"{a['title']} {a['summary']}", filter_kws)]
    print(f"キーワード一致: {len(filtered)}件")

    # dedup
    today = datetime.now(JST).strftime("%Y-%m-%d")
    new_articles = []
    for a in filtered:
        h = url_hash(a["url"])
        if h not in seen:
            new_articles.append(a)
            seen[h] = today

    print(f"新規(重複除去後): {len(new_articles)}件")

    # write digest
    DIGEST_FILE.write_text(generate_digest(new_articles), encoding="utf-8")
    print(f"\ndigest.md を出力しました")

    save_seen_urls(seen)

    # Slack 通知
    alert_articles = [a for a in new_articles if matches_any(f"{a['title']} {a['summary']}", alert_kws)]
    bot_token  = os.environ.get("SLACK_BOT_TOKEN", "")
    channel_id = os.environ.get("SLACK_CHANNEL_ID", "")
    github_token = os.environ.get("GITHUB_MODELS_TOKEN", "")

    if bot_token and channel_id:
        notify_slack(new_articles, alert_articles, bot_token, channel_id, github_token)
    else:
        print("  Slack: SLACK_BOT_TOKEN または SLACK_CHANNEL_ID 未設定のためスキップ")


if __name__ == "__main__":
    main()
