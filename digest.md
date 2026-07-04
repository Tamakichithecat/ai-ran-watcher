# 📡 AI RAN Digest — 2026-07-04

収集日時: 2026-07-04 21:40 JST | 新規記事: 5件
🔴標準化:1　📄論文:1　🏢企業:1　🇯🇵国内:1　📰海外:1

> ℹ️ 本日のRAWリスト（digest_raw.md）は0件（最終更新 2026-06-06）のため、Web検索による補完で本Digestを生成しています。前回Digest（2026-06-28）に未掲載の記事のみを採録し、URL重複を避けています。各記事の実公開日を本文に明記しています。

## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）

🔺 **Analysis: Cohere's $28M U.S. DoD FutureG ISAC Contract; OTFS vs OFDM; 6G-NR/IMT 2030 RIT Standards Outlook**
   IEEE ComSoc Technology Blog（2026年7月2日） | https://techblog.comsoc.org/2026/07/02/analysis-coheres-28m-u-s-dod-futureg-isac-contract-otfs-vs-ofdm-6g-imt-2030-standards-outlook/
   • 米国防総省（DoW）傘下のFutureG Officeが、Cohere Technologiesの独自波形Zak-OTFS（Pulsone）を用いたISAC（通信・センシング統合）マルチ波形RANプロトタイプ開発に2800万ドルを拠出。ドローン検知・追跡を主目的とする。
   • 3GPPは6G NR（IMT-2030 RIT申請）についてOFDM系波形を基本方針とする見通しが強く、OTFSは高ドップラー環境やNTN、ISACなど限定用途での採用検討にとどまる可能性が高いと分析。
   • ITU-R WP5DはIMT-2030のRIT候補提案を2027年2月～2029年2月の期間で募集中であり、OTFSが正式な6G標準波形として採用されるかは今後の技術評価・業界コンセンサス次第。

## 📄 論文・技術文書（IEEE Xplore等）

🔺 **From RAN Control to Agentic Intelligence: Architecture and Vision for Energy Efficient AI-RAN**
   著者😎：Sabrine Aroua、Alexis I. Aravanis、Ilias Chatzistefanidis、Hamza Abbar、Anh-Khoa Dang、Anastasios Giovanidis、Salah-Eddine El Ayoubi、Stephane Senecal、Martha Vlachou Konchylaki、Navid Nikaein（Ericsson Research / Orange Innovation / EURECOM / BubbleRAN 他）
   arXiv（2606.21955、IEEE Network Magazine査読中） | https://arxiv.org/pdf/2606.21955
   • 6GではAI-RAN（通信基盤とAI処理基盤の共用化）が高密度展開と常時AI処理により、RANの消費電力を大幅に増加させると指摘。
   • 既存のO-RAN（RIC・SMOによるプログラマブル制御）はポリシー駆動が中心で、複数アプリケーション間の適応的な省電力連携には限界があると分析。
   • LLM駆動のセマンティック・インテント抽象化を用いた「エージェント型AI-RAN」アーキテクチャを提案し、異種ワークロード間の適応オーケストレーション・競合解決・省エネ多目的最適化の実現構想を提示。

## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank）

🔺 **SoftBank Establishes "SB Neo" to Launch Neocloud Business in the U.S., Backed by 10-Gigawatt-Scale Energy and AI Infrastructure**
   企業名🏢：SoftBank Corp. / SoftBank Group Corp.
   SoftBank 企業・IR（2026年7月2日） | https://www.softbank.jp/corp/news/press/sbkk/2026/20260702_01/
   • ソフトバンクとソフトバンクグループが、米国でネオクラウド事業を展開する新会社「SB Neo, Inc.」（出資比率51%：49%）を2026年7月に設立。
   • グループが開発中の10ギガワット規模のエネルギー・AIインフラを基盤に、大規模AIモデルの学習・推論向け計算資源を米国の大企業・ハイパースケーラー向けに2027年度から提供予定。
   • 日本で提供中のAIデータセンター向けソフトウエアスタック「Infrinia AI Cloud OS」のノウハウを活用する方針で、AI-RANを含むグループ全体のAIインフラ拡大戦略の一環と位置づけられる。

## 🇯🇵 日本語メディア

・ **ソフトバンクが米国にネオクラウドの新会社「SB Neo」を設立**
   メディア名📰：BUSINESS NETWORK（2026年7月2日）
   BUSINESS NETWORK | https://businessnetwork.jp/article/35764/
   • ソフトバンクが米国オハイオ州の「PORTS Technology Campus」を中核に、発電容量とデータセンターを直結させる垂直統合型AIインフラを整備する計画と報道。
   • SB Neoはハイパースケーラー等へのGPU計算資源提供（ネオクラウド）を担い、2027年度のサービス開始を目指す。
   • 孫正義氏は「グループを挙げて世界最高水準のAIインフラを展開し、AI革命を推進する」とコメントし、日本国内でもギガワット級AIデータセンター構築を進める方針を表明。

## 📰 業界・一般メディア（英語）

🔺 **Dell'Oro: AI RAN Revenue Forecast: $35B from 2026-to-2030; 3 Types of AI RAN Explained**
   メディア名📰：IEEE ComSoc Technology Blog（2026年6月30日、Dell'Oro Group調査）
   IEEE ComSoc | https://techblog.comsoc.org/2026/06/30/delloro-ai-ran-revenue-forecast-35b-from-2026-to-2030-3-types-of-ai-ran-explained/
   • 調査会社Dell'Oroが、2026～2030年の累積AI RAN市場規模を350億ドルと予測。ただしAI RANが従来型RAN市場全体を拡大させる可能性は低いと指摘。
   • 短期的にはAI-for-RAN（AIによるRAN最適化）、シングルパーパス型展開、非GPUアーキテクチャ、D-RAN・5G向けが市場の中心になると分析。
   • GPUを用いたAI-and-RAN（GPU RAN）型は予測期間末までに10億ドル超規模へ成長すると上方修正されたが、依然として市場全体の一部にとどまる見通し。

---
*このDigestはAI RANウォッチャーが自動生成しています。*
