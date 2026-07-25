# 📡 AI RAN Digest — 2026-07-25

収集日時: 2026-07-25 10:24 JST | 新規記事: 7件
🔴標準化:1　📄論文:1　🏢企業:1　🇯🇵国内:1　📰海外:3

## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）

🔺 **59 New or Updated O-RAN Technical Documents Released Since March 2026**
   O-RAN ALLIANCE Blog | https://www.o-ran.org/blog/59-new-or-updated-o-ran-technical-documents-released-since-march-2026
   • 2025年11月以降、O-RAN ALLIANCEの各WG/FGが技術文書計157件のうち59件（新規10件含む）を公開・更新。
   • Near-RT RIC向けR1インターフェースでAI/MLモデルの学習・展開APIとデータアクセスAPIを拡充し、massive-MIMO最適化やD2インターフェース（DU間キャリアアグリゲーション）も追加。

## 📄 論文・技術文書（IEEE Xplore等）

🔺 **AI-RAN on NPUs: Baseband Processing Without Baseband Chips**
   著者😎：Shilong Zhang, Luping Xiang, Jienan Chen, Kun Yang
   arXiv | https://arxiv.org/pdf/2607.04224
   • 専用ベースバンドチップを使わず、NPU（AIアクセラレータ）上でOFDM送受信機を構成する新方式を提案。
   • Ascend 310B1エッジNPUとUSRP X300（3.0GHz帯）を用いた実機実証により、AI推論と無線信号処理を同一ハードウェア上に統合できることを確認した。

## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank）

🔺 **AI-RANを実証から商用展開へ**
   企業名🏢：SoftBank
   ソフトバンクニュース | https://www.softbank.jp/sbnews/entry/2026/07/16/160000_1
   • ソフトバンクが自社のAI-RAN技術「AITRAS」を実証段階から商用展開段階へ移行すると発表。RAN制御機能とAIサーバー機能を同一の汎用サーバー上で実現する構想。
   • 2026年中に自社商用ネットワークへの本格導入を進め、国内外の通信事業者への展開も視野に入れる。

## 🇯🇵 日本語メディア

🔺 **総務省、NVIDIA社とのフィジカルAI接続基盤となる6G及びAI RAN関連技術に関する協力意向表明書に署名**
   メディア名📰：総務省（報道資料）
   総務省 | https://www.soumu.go.jp/menu_news/s-news/01tsushin06_02000350.html
   • 総務省が2026年7月16日、NVIDIA社との間で6G及びAI-RAN関連技術に関する協力の戦略的目標・協力予定分野を確認する意向表明書に署名。
   • 2026年2月のAI-RAN Alliance参画に続く取り組みで、6G・AI-RAN分野における日本の国際競争力確保と技術の社会実装・海外展開を目指す。NVIDIA側はテレコム事業部門のRonnie Vasishta氏（Senior Vice President）が署名した。

## 📰 業界・一般メディア（英語）

🔺 **South Korea launches AI-RAN project to advance industrial AI**
   RCR Wireless News | https://www.rcrwireless.com/20260722/5g/south-korean-ai-ran
   • 韓国情報社会振興院（NIA）がSKテレコムとKT率いる2つのコンソーシアムを選定し、総額172億ウォン（約1,160万ドル）の「Hyper AI Network Infrastructure」実証事業を開始。
   • AI-RANとスタンドアロン5Gを組み合わせ、溶接・塗装・巡回ロボットなど産業用フィジカルAIを支援。2027年以降はヒューマノイドロボット実証も計画し、Samsung Networks、Nokia、Ericsson、HFRの機材を活用する。

・ **Red Hat outlines AI-RAN roadmap**
   RCR Wireless News | https://www.rcrwireless.com/20260717/carriers/red-hat-outlines-ai-ran
   • Red HatのShujaur Mufti氏が、AI-RANは「AI for RAN→AI and RAN→AI on RAN」の3段階で進化すると説明。2027年頃までは既存RAN上での省エネ・スペクトル効率向上等の活用が中心になるとした。
   • GPUをRAN全域に導入するのではなく、経済合理性の高い一部拠点から段階的に採用すべきと指摘。SoftBank・Fujitsu・NVIDIAとの実証で、L1/L2処理をリアルタイムカーネル無しで実行できることを確認済みとした。

・ **The Agentic Network — Rakuten Mobile on turning data into outcomes**
   RCR Wireless News | https://www.rcrwireless.com/20260723/carriers/agentic-network-rakuten-mobile
   • 楽天モバイルCDAOのSachin Verma氏が、RAN Intelligent Controller（RIC）上で動くrAppが機械学習でネットワーク挙動を予測し閉ループで自動制御する仕組みを説明。
   • 日本全国でRAN省エネ機能（TM Forum Level 4認証取得済み）を展開し、年間約17〜20%の電力削減と年間約10億円規模のコスト削減を実現。異常検知・原因分析は自動化済みだが、是正措置の自動化は開発中とした。
