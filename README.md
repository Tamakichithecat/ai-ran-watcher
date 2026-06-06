# 📡 AI RAN Watcher

AI RAN / AI Native RAN に関するニュース・論文・標準化動向を毎日自動収集し、Slackに通知するパーソナル情報収集システム。

---

## ワークフロー整理表

| # | 実行者 | ワークフロー / タスク名 | 実行時刻 | トリガー | 処理内容 | 出力先 |
|---|---|---|---|---|---|---|
| ① | GitHub Actions | `daily.yml` | **7:00 JST** | cron（毎日） | RSS・スクレイピングで記事収集<br>キーワードフィルタ・重複除去 | `digest_raw.md`<br>`seen_urls.json` |
| ② | Cowork<br>（Claude Scheduled Task） | AI RAN Digest タスク | **7:15 JST** | cron（毎日） | `digest_raw.md` を読み込み<br>Web検索で記事補完<br>重要度評価・日本語サマリー生成 | `digest.md`<br>（GitHub commit） |
| ③ | GitHub Actions | `notify.yml` | **~7:20 JST** | `digest.md` への push | `digest.md` を解析<br>Slackにメイン通知＋スレッド投稿 | Slack |

> **補足:** ③は `github-actions[bot]` によるpushでは発火しない。Cowork（②）のcommitでのみ起動する。

---

## Slack通知の構成

```
[メインメッセージ]
@here 📡 AI RAN Daily — YYYY-MM-DD
新規記事: N件 | カテゴリ別件数
トップ10件: タイトル＋リンク一覧

  └─ [スレッド × 10件]
       記事タイトル・リンク
       • 日本語要点1（Cowork生成）
       • 日本語要点2
       🤖 Claudeで深掘り → claude.ai/new?q=...
```

---

## ファイル構成

```
ai-ran-watcher/
├── .github/workflows/
│   ├── daily.yml        # ① 毎朝7:00 記事収集
│   └── notify.yml       # ③ digest.md push時にSlack通知
├── collector.py         # 記事収集・フィルタリング処理
├── notifier.py          # Slack通知処理
├── sources.yaml         # 収集ソース設定（ON/OFF管理）
├── keywords.yaml        # フィルタ・アラートキーワード設定
├── digest_raw.md        # ① の出力（収集データ）
├── digest.md            # ② の出力（Cowork拡充済みデータ）
└── seen_urls.json       # 重複除去キャッシュ（30日保持）
```

---

## ソース管理

`sources.yaml` の `enabled` を `true/false` に変更してpushするだけでソースを追加・停止できる。

| カテゴリ | 主なソース |
|---|---|
| 標準化 | 3GPP, O-RAN Alliance, AI RAN Alliance, ITU, ETSI, IEEE SA |
| 論文 | IEEE Communications Magazine, IEEE Network, IEEE Transactions on Wireless |
| 企業PR | NVIDIA / T-Mobile / SoftBank（Google News経由） |
| 日本語メディア | 日経クロステック, ITmedia Mobile, ケータイ Watch |
| 英語メディア | RCR Wireless, Light Reading, Fierce Wireless |

---

## キーワード管理

`keywords.yaml` で2種類のキーワードを管理する。

| 種別 | 用途 |
|---|---|
| `filter_keywords` | 収集対象の絞り込み（AI RAN, O-RAN, xApp など） |
| `alert_keywords` | 重要記事の検出（3GPP Release 19, AI RAN Alliance など） |

---

## 必要なGitHub Secrets

| Secret名 | 用途 |
|---|---|
| `SLACK_BOT_TOKEN` | Slack Bot API認証（`xoxb-...`） |
| `SLACK_CHANNEL_ID` | 通知先チャンネルID |
| `GITHUB_MODELS_TOKEN` | GitHub Models API認証（PAT） |
| `CLAUDE_PROJECT_URL` | CoworkのURL（Slackリンク用・任意） |
