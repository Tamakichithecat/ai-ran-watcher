# 📡 AI RAN Digest — 2026-09-22

収集日時: 2026-09-22 08:38 JST | 新規記事: 5件
🔴標準化:1　📄論文:1　🏢企業:2　🇯🇵国内:0　📰海外:1

## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）

🔺 **Working Group Reports to RAN Plenary #113（Madrid）**
   3GPP News | https://www.3gpp.org/news-events/3gpp-news/ran113-reports
   • 3GPP TSG RANの第113回総会（マドリード開催）に合わせ、RAN1〜RAN5の各ワーキンググループがAI/ML関連ワークアイテムの進捗を報告。NR空中インタフェース向けAI/ML拡張（WI）が新規承認され、NG-RAN向けAI/ML Phase3は進捗30%→50%、モビリティ向けAI/ML（NR_AIML_Mob）は50%→65%に前進。
   • 6G無線（6GR）については、アップリンク符号化（BG3）、コンステレーションシェーピング、高次変調、6GR用同期信号ブロック（SSB）設計などで節目の進捗があったと報告。Multi-RAT Spectrum Sharing（MRSS、5G/6G間の周波数共用方式）の暫定性能評価もRAN1から提示された。
   • RAN3は6G RANアーキテクチャの上位レイヤ分割（HLS）について、CU-DU分割・CP-UP分離を含む5G方式をベースラインとすることで合意。AI/ML関連ワークアイテムはいずれも2027年3月を目標に作業が継続する。

## 📄 論文・技術文書（IEEE Xplore等）

🔺 **Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN**
   著者😎：Seyed Bagher Hashemi Natanzi, Bo Tang
   arXiv | https://arxiv.org/abs/2609.18857
   • O-RANの制御プレーンでは異なるベンダー製の自律AIエージェント（rApp）が共有無線リソースを個別に制御し始めているが、SLA維持を狙うエージェントと省電力のため利用率最大化を狙うエージェントが競合し、リソース配分が振動する問題を指摘。
   • 論文はAURA（Arbitrated aUtonomous Resource Agents）という軽量な調停レイヤーを提案。各エージェントの内部ロジックを知らなくても、提案された制御アクションを「実現可能性」「変更間隔」「変化量の閾値」の3条件で仲裁し、SLA関連の変更を優先させる仕組み。
   • OpenAirInterface／FlexRICを用いたO-RAN実機テストベッドで実測トラフィックにより検証し、リソース配分が安定した動作点に収束することを確認した。

## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank）

🔺 **AT&T, T-Mobile, Verizon take different roads to AI-RAN**
   企業🏢：AT&T, T-Mobile, Verizon
   Communications Today | https://www.communicationstoday.co.in/att-t-mobile-verizon-take-different-roads-to-ai-ran/
   • 米国大手3社がAI-RANの実装方針で分裂。VerizonはGPUを使わずCPUベース無線機にAI推論を組み込む方式を採用し、仮想化基地局（vRAN）約22,900局、Open RAN対応無線機17万台超を既に展開。
   • T-MobileはNokia・NVIDIAと連携しGPU中心のAI-RAN構想を推進。米ベルビューにAI-RANイノベーションセンターを設置し、2026年中にNokia製GPU無線機の試作機納入を予定。
   • AT&Tは高コスト・複雑性を理由にGPU方式へ懐疑的で、Verizonに近い立場。Ericssonと共同でGPUを使わないAIネイティブ・スケジューラの検証も進めている。

🔺 **US telcos diverge on AI-RAN GPU deployment strategy: Report**
   企業🏢：AT&T, T-Mobile, Verizon
   ET Telecom (Google News) | https://news.google.com/rss/articles/CBMi0gFBVV95cUxPcVdVTndNZHY5UHdZamF4VllPSFFOb0hqcjJQc1AzdEFJZXdYNVlEaENmUEN0WnYyM1dCSFdmMmpBOHNfRTdfRmdMSW1DM0VjNW5mMW1USnBfdGQzbDRDNG9BNUFLUkJVVlNxSkNVd210Q09mM2ExMmFVVFJ1bnIzMnRfVGp3aTQ2YnM2NF82V29PR1dqWlRUcWVBZ0ZETFRlMUJkYmtaQjlQempCZU1fWmJPdVZHM0p4UnNWRVpidFdfTFVzS3VjN0d3SVRrSjRWWHfSAdcBQVVfeXFMUGdqTElTQkV5dzBnaERtRFRrMHI3ZHZKUGRvc202M2k1WUV2WnZqN0Nkb2xpNWtYdlBVZDI1Tzh4WHZQaXNMTnppLVJ5SjBFWXE5dVV4RDZibUVCNzhPdnNDTkExQ0ZGb3Y1WFJsdG90ZG9zNjlac0NFMnlwSlFTcGpFcjM1eXdyUkRhdklxNW9FTTJSMVNXekJ5SFVDWEVWVkJtXzQ0R0NnZ3Y3eEMxNUI0YjFFendpRGRxQ09ITm1XTW9Ya1RPcExnNVRudGh5ZG94SU93Mzg?oc=5
   • GPUを無線機内に搭載するか否かで各社の戦略が分岐。T-MobileはGPU活用を志向する一方、Ericssonと共同でGPUを使わないAIネイティブ・スケジューラの大規模実証をロサンゼルス・ニューヨーク・ニュージャージー・ソルトレイクシティ等の約43サイトで実施中。
   • AT&TはセルサイトへのGPU配備を当面見送り、AI推論は地域データセンター側で実施する方針。2023年のEricssonとの140億ドル規模Open RAN契約を軸に検証を継続。
   • Verizonは引き続きGPU方式に最も懐疑的な立場を維持している。

## 📰 業界・一般メディア（英語）

・ **AI-Native Telecom Market Poised for Rapid Growth Through 2032**
   メディア名📰：GlobeNewswire（Research and Markets）
   GlobeNewswire | https://www.globenewswire.com/news-release/2026/09/18/3364521/28124/en/ai-native-telecom-market-poised-for-rapid-growth-through-2032-as-intelligent-networks-automated-infrastructure-and-next-generation-solutions-transform-connectivity.html
   • 調査会社Research and Marketsが、AIネイティブ通信インフラ・インテリジェントネットワーク市場の分析レポートを公表。市場規模は2026年時点で約80.7億ドルと推計され、2032年まで二桁成長が続くと予測。
   • AI-RAN、エージェント型AIオーケストレーション、ソブリンAI基盤、NaaS（Network as a Service）が主要な成長領域として挙げられ、無線アクセスネットワークからコア・エッジ・トランスポート層まで全レイヤーでAI活用が進むと分析。
   • 主要プレイヤーとしてNVIDIA、Huawei、Ericsson、Nokiaに加えMicrosoft・Google・AWS等のクラウド事業者、Mavenir・Subex等の専業ベンダーを列挙。レガシー網との統合コストや人材不足が課題として指摘されている。
