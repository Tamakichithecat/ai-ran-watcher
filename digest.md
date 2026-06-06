# 📡 AI RAN Digest — 2026-06-06

収集日時: 2026-06-06 21:29 JST | 新規記事: 10件（累計21件）
🔴標準化:4　📄論文:3　🏢企業:7　🇯🇵国内:4　📰海外:3

---

## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）

🔺 **3GPP TSGs#112 Plenary Meeting — Singapore (June 8–12, 2026)**
   3GPP | https://www.3gpp.org/news-events/3gpp-news/singapore-1
   • シンガポール・Marina Bay Sandsで3GPP第112回全体会合が開催（6/8〜12）、3GPPにとって初のシンガポール開催。
   • Release 21（6G）タイムラインの正式承認が主要議題のひとつ、ASN.1/OpenAPI凍結は最早でも2029年3月以降。
   • RAN3は6G RAN-Core間インターフェース（P2P vs SBI）およびCU-DU・CP-UPスプリット方針を審議予定。

🔺 **3GPP Completes Release 19, Progress Begins on 6G Work**
   FirstNet | https://firstnet.gov/newsroom/blog/3gpp-completes-release-19-while-progress-begins-6g-work
   • Rel-19 Stage 3仕様が2025年9月に、RAN4性能仕様が2026年3月に凍結完了。
   • AI/ML機能はRAN1（CSI予測・ビーム管理）、RAN2（モビリティ）、RAN3（NG-RAN）全WGで仕様化。
   • 6G無線研究フェーズ（TR 38.914）が2026年6月に完了予定、Rel-21 Work Item化へ移行。

🔺 **O-RAN ALLIANCE F2F Meeting + nGRG/ISAC Workshop — Seattle (June 1–5, 2026)**
   O-RAN ALLIANCE | https://www.o-ran.org/events
   • シアトルでO-RAN F2F会合（6/1〜5）を実施、既存5G網向けO-RAN仕様の統合作業が主軸。
   • 6/4にnGRG（次世代研究グループ）とISAC（統合センシング・通信）合同ワークショップを開催。
   • DeepSig等がOpenRAN上でのAI-RANとISAC開発加速に関するプレゼンを実施。

🔺 **Metanoia Becomes First Silicon Vendor in O-RAN Alliance WG7 Reference Architecture — COMPUTEX 2026**
   Business Standard / PRNewswire | https://www.business-standard.com/content/press-releases-ani/metanoia-showcases-ai-ran-ecosystem-and-launches-breakthrough-5g-open-sdr-platform-at-computex-2026-126060400354_1.html
   • MetanoiaがO-RAN WG7のホワイトボックスリファレンス設計アーキテクチャに組み込まれた初のシリコンベンダーに認定（FR1 24 dBm・5W O-RU、FR2 50 dBm審査中）。
   • COMPUTEX 2026（台北）にて5G Open SDRプラットフォームとAI-RAN対応5G DUサーバの統合をライブデモ。
   • オープンソースSDR基盤「MOSART（Metanoia Open Source Advanced Radio Technology）」を商用リリース、O-RAN PlugFest Spring 2026での相互接続検証後に正式展開。

---

## 📄 論文・技術文書（arXiv / IEEE Xplore等）

・ **Advanced AI Service Provisioning in O-RAN through LLM Engine Integration**
   arXiv | https://arxiv.org/abs/2605.23809
   • O-RAN上でLLMベースのオーケストレータと自動MLエンジンを組み合わせた「Dual-Brain」アーキテクチャを提案。
   • Non-RT RICにLLMを配置し、ネットワーク意図を自動的にxApp制御ポリシーへ変換する仕組みを実証。

・ **Agentic AI-RAN: Enabling Intent-Driven, Explainable and Self-Evolving Open RAN Intelligence**
   arXiv | https://arxiv.org/abs/2602.24115
   • Plan-Act-Observe-Reflectの自律エージェント原則をO-RANに適用し、スライスライフサイクル管理と無線リソース管理を自動化。
   • マルチセルO-RANシミュレーションで従来手法比でKPI改善を実証。

・ **Towards AI-Driven RANs for 6G and Beyond: Architectural Advancements and Future Horizons**
   arXiv | https://arxiv.org/abs/2506.16070
   著者😎：Mathushaharan Rathakrishnan, Samiru Gayan, Rohit Singh, Amandeep Kaur, Hazer Inaltekin, Sampath Edirisinghe, H. Vincent Poor
   • 6G RANのAI駆動化に向けた新しいAI-RANフレームワークを提案、インテリジェントオーケストレーションとリソース最適化シナリオで評価。
   • デジタルツイン・IRS（インテリジェント反射面）・大規模生成AIモデルをRAN主要イネーブラとして考察。
   • ISAC（統合センシング・通信）とAgentic AIを組み合わせた将来の研究方向性を提示。

---

## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank / Nokia 等）

🔺 **NVIDIA and Global Telecom Leaders Commit to Build 6G on Open and Secure AI-Native Platforms**
   NVIDIA Newsroom | https://nvidianews.nvidia.com/news/nvidia-and-global-telecom-leaders-commit-to-build-6g-on-open-and-secure-ai-native-platforms
   • MWC 2026（3/1）にてNVIDIA主導でSoftBank・T-Mobile・Nokia・Ericsson・Deutsche Telekom等12社が6G AI-native基盤構築へ共同コミット。
   • オープン・セキュア・AI-nativeの原則に基づき、RAN・エッジ・コアにAIを統合したソフトウェア定義ネットワークを推進。
   • AI-RAN Allianceには130社以上が参加し、商用展開フェーズへの移行を宣言。

🔺 **NVIDIA and Nokia to Pioneer the AI Platform for 6G — Powering America's Return to Telecommunications Leadership**
   NVIDIA Newsroom | https://nvidianews.nvidia.com/news/nvidia-nokia-ai-telecommunications
   • NVIDIAとNokiaが6G向けAIプラットフォームのパイオニアとして共同開発を発表、米国の通信リーダーシップ回復を目標に掲げる。
   • NokiaのanyRANソフトウェアとNVIDIA AI Aerialを組み合わせ、T-MobileがパイロットとしてAI-RANインフラを展開中。
   • 5Gから6GへのソフトウェアアップグレードによるAI-native化を実現するアーキテクチャを提示。

🔺 **NVIDIA, T-Mobile and Partners Integrate Physical AI Applications on AI-RAN-Ready Infrastructure**
   NVIDIA Newsroom | https://nvidianews.nvidia.com/news/nvidia-t-mobile-and-partners-integrate-physical-ai-applications-on-ai-ran-ready-infrastructure
   • T-MobileがNVIDIA AI-RANインフラ上で物理AIアプリケーション（ロボット制御・自律システム等）の統合を実証。
   • RANとAIワークロードの共有コンピューティング基盤により、エッジAIの遅延を最小化しつつ通信品質を維持。
   • NVIDIA Physical AIパートナーエコシステムとT-Mobile網の組み合わせで産業用途へのAI-RAN展開を加速。

・ **Nokia and Orange Advance AI-RAN Innovation with NVIDIA**
   Nokia Newsroom | https://www.nokia.com/newsroom/nokia-and-orange-advance-airan-innovation-with-nvidia/
   • NokiaとOrangeがNVIDIAのAIインフラを活用したAI-RANユースケースの共同開発・共同イノベーション協定を締結。
   • AI-native 6Gに向けたユースケース共創を目的に、anyRANソフトウェアとNVIDIA GPU基盤の組み合わせを実証予定。

・ **AI-RAN Alliance Reaches Major Milestone — 132 Members, New Board Members from Qualcomm/SKT/Vodafone**
   Yahoo Finance / HPCwire | https://finance.yahoo.com/news/ai-ran-alliance-reaches-major-152400894.html
   • 設立から約2年でグローバル132会員に拡大、Qualcomm・SK Telecom・VodafoneがBoard Memberに加入。
   • 4つの基盤技術文書（リファレンスアーキテクチャ・AI/MLモデル手法・インフラオーケストレーション・AI-on-RAN）を公開。
   • MWC 2026で33件のAI-RANデモと4つの新産業ブループリントを披露、実験フェーズから商用展開フェーズへ転換を宣言。

・ **NVIDIA and US Telecom Leaders Unveil the All-American AI-RAN Stack to Accelerate the Path to 6G**
   NVIDIA Newsroom | https://nvidianews.nvidia.com/news/nvidia-us-telecom-ai-ran-6g
   • GTC Washington D.C.（2025/10）にてBooz Allen・Cisco・MITRE・ODC・T-Mobileと共同で米国初のAI-native 6Gワイヤレスプラットフォームを発表。
   • NVIDIA AI Aerialプラットフォーム上でISACアプリとAI駆動スペクトラム管理アプリを実証。
   • ODCのソフトウェア定義5G RANが従来比7倍のセル容量・3.5倍の電力効率を達成。

・ **Nvidia-Led AI-RAN Alliance to Hold Annual Assembly in Seoul in November**
   Seoul Economic Daily | https://www.sedaily.com/
   • NVIDIA主導のAI-RAN AllianceがNovemberにソウルで年次総会を開催予定。
   • アジア太平洋地域での展開加速と会員拡大が目的。

---

## 🇯🇵 日本語メディア

・ **【解説】AI-RAN：AIエラを支える社会インフラ（SoftBank Research Institute of Advanced Technology）**
   SoftBank | https://www.softbank.jp/en/corp/technology/research/topics/122/
   • SoftBankがAI-RANのコンセプト（AI for RAN・AI on RAN・AI and RAN）と6Gへの展望を解説。
   • 同一ハードウェア上でRANとAIサーバ機能を並列実行し、超低遅延・大容量・セキュアなAIアプリを実現する構成を提示。

・ **SoftBank、自社LLM「Sarashina」をOracle Alloy基盤クラウドで提供開始（2026年6月〜）**
   SB Intuitions | https://www.sbintuitions.co.jp/en/news/press/20260416_01/
   メディア名📰：SB Intuitions（SoftBank子会社）
   • SoftBank子会社SB Intuitionsが国産LLM「Sarashina」をOracle Alloy利用の「Cloud PF Type A」上でエンタープライズ向けに提供開始（2026年6月）。
   • SoftBank国内データセンター内に閉じた環境でデータ主権・セキュリティ要件に対応した生成AIサービスを実現。
   • 文書校正・レポート自動生成・プログラミング支援・マルチエージェントシステム構築等のユースケースをカバー。

・ **KDDI Research、Nokiaと6G向け「4次元リソース最適化技術」の実証に成功 — 同スループット比で消費電力40%削減**
   KDDI Research | https://www.kddi-research.jp/english/newsrelease/2026/052001.html
   メディア名📰：KDDI Research（2026年5月20日）
   • KDDI ResearchとNokia Bell Labs（米国・マレーハイル）が「Intelligent 4D Resource Optimization Technology」の商用5Gエミュレーション環境で実証に成功。
   • 時間・周波数・空間・電力の4次元を動的制御し、同スループット比で最大40%の消費電力削減、または同電力比で最大4倍のスループット向上を達成。
   • 同日（4/23）NokiaとKDDI Researchが追加の省エネ研究に向けた共同研究協定を締結。

・ **KDDIが3年間AI/6G計画「Power-to-Connect 2028」を発表、1.2兆円投資**
   Telecomstechnews | https://www.telecomstechnews.com/news/kddi-ai-infrastructure-plan-6g-network-automation/
   メディア名📰：Telecomstechnews / KDDIニュースルーム（2026年4月）
   • KDDIが2026年4月〜2029年3月を対象とする3カ年計画「Power-to-Connect 2028」を発表、AIインフラ・低遅延ネットワーク・AIデータセンターに1.2兆円を投資。
   • EricssonとのAI駆動アップリンク干渉最適化アプリの商用網フィールドトライアルで4G/5G混在環境の上りリンク性能改善を確認。
   • 6G無線研究（Nokia共同）と並行して、ネットワーク自動化・デジタルツインの商用展開を進める方針。

---

## 📰 業界・一般メディア（英語）

・ **GTC 2026: Nvidia Wants to Reinvent the RAN**
   Data Center Dynamics | https://www.datacenterdynamics.com/en/analysis/nvidia-wants-reinvent-the-ran-gtc-2026/
   メディア名📰：Data Center Dynamics
   • NVIDIAがGTC 2026でRANのソフトウェア定義化を核心とするAI-RANビジョンを提示、「6Gはソフトウェアアップグレードで実現可能」と主張。
   • NVIDIA AI Aerialプラットフォームベースのオープンスタックが従来ベンダーロックイン型RANへの代替として訴求。

・ **5G Standards Groups Scuffle for the AI Advantage**
   Light Reading | https://www.lightreading.com/ai-machine-learning/5g-standards-groups-scuffle-for-the-ai-advantage
   メディア名📰：Light Reading
   • 3GPP・O-RAN Alliance・AI-RAN Allianceの3団体が6G AI標準化の主導権をめぐり競合・協調する動向を分析。
   • 各団体の仕様が重複・補完する領域とインターオペラビリティ確保に向けた調整の現状を解説。

・ **Ericsson and Nokia Are Diverging Like Never Before on AI-RAN**
   Light Reading | https://www.lightreading.com/5g/ericsson-and-nokia-are-diverging-like-never-before-on-ai-ran
   メディア名📰：Light Reading
   • NokiaはNVIDIAとの密接な提携を5G/6G戦略の核心に据える一方、EricssonはAI-RANにおける独自性・独立路線を堅持。
   • EricssonはAI推論をRANスタック内部に組み込む垂直統合モデル、NokiaはanyRAN+NVIDIAのオープンスタックモデルという戦略的分岐が鮮明化。
   • 両社の分岐は通信キャリアのベンダー選択とエコシステム戦略に重大な影響を与えると分析。

---
*このDigestはAI RANウォッチャーが自動生成しています。*
