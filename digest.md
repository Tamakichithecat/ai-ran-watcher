# 📡 AI RAN Digest — 2026-07-05

収集日時: 2026-07-05 21:20 JST | 新規記事: 5件
🔴標準化:1　📄論文:1　🏢企業:1　🇯🇵国内:1　📰海外:1

> ℹ️ 本日のRAWリスト（digest_raw.md）は0件（最終更新 2026-06-06）のため、Web検索による補完で本Digestを生成しています。前回Digest（2026-07-04）に未掲載の記事のみを採録し、URL重複を避けています。厳密な過去7日以内では十分な新規AI RAN記事が確認できなかったため、直近3週間程度まで範囲を広げて重要記事を選定しました。各記事の実公開日を本文に明記しています。

## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）

🔺 **3GPP Approves Timelines for Release 21 Which Will Specify 6G RAN, Core and 5G-Advanced**
   IEEE ComSoc Technology Blog（2026年6月16日） | https://techblog.comsoc.org/2026/06/16/3gpp-approves-timelines-for-release-21-which-will-specify-6g-ran-and-5g-advanced/
   • 3GPPのTSG RAN#112会合（シンガポール開催）で、Release 21の作業タイムラインが正式承認された。
   • Release 21では6G RANおよび5G-Advancedの技術仕様を策定し、最初の機能凍結（Functional Freeze）を2027年3月、2回目の凍結を2028年6月に予定。
   • 3GPPは6GをAIネイティブ設計と位置づけており、AI/MLをRelease 21の仕様策定当初から組み込む方針が示されている。

## 📄 論文・技術文書（IEEE Xplore等）

🔺 **GENESIS: Harnessing AI Agents for Autonomous 6G RAN Synthesis, Research, and Testing**
   著者😎：Tamerlan Aghayev、Maxime Elkael、Michele Polese、Minh Dat Nguyen、Gabriele Gemmi、Andrea Lacava、Ali Saeizadeh、Reshma Prasad、Paolo Testolina、Angelo Feraudo、Soumendra Nanda、Pedram Johari、Salvatore D'Oro、Tommaso Melodia（Northeastern University）
   arXiv（2605.27360、2026年6月4日発表） | https://arxiv.org/pdf/2605.27360
   • Northeastern大学の研究チームが、3GPP仕様に基づくRAN機能の実装・試験・最適化・セキュア化を人手を介さず自動で行う「エージェント型AI」フレームワークGENESISを発表。
   • 従来は専門エンジニアが数ヶ月を要していた3GPP条項から実機（Over-the-Air）検証済みコードへの実装工程を、数時間で完了できることを実証。
   • 5G機能実装タスクの比較実験では、GENESISが複数回の独立試行で100%の成功率を達成した一方、既存の汎用コーディングAIエージェント（ベースライン）は一度も動作するコードを生成できなかった。

## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank）

🔺 **KDDI, KDDI Research and Global Partners Launch RAN Digital Twin Collaboration for the 6G Era**
   企業名🏢：KDDI Corporation / KDDI Research, Inc.（NVIDIA、Keysight Technologies、Samsung Research Americaと協業）
   KDDI News Room（英語版）（2026年6月23日） | https://newsroom.kddi.com/english/news/detail/kddi_nr-1068_4588.html
   • KDDIとKDDI総合研究所が、NVIDIA・Keysight Technologies・Samsung Research Americaと共同で、6G時代に向けた高精度「RANデジタルツイン」構築の協業を開始すると発表。
   • NVIDIAのAerial Omniverse Digital Twin（AODT）とKeysightのUE（端末）エミュレーション技術を活用し、KDDIの実網データをもとに仮想空間上でRANを再現する基盤を開発する。
   • 2028年度末までにスケーラビリティ実証プロトタイプを構築し、2030年度末までにKDDI商用網での性能検証を目指す。複数の自律型AIエージェントによるRAN「What-if」シナリオの安全な検証などへの活用を想定。

## 🇯🇵 日本語メディア

🔺 **KDDIやNVIDIAら5社、6G時代に向け「デジタルツインRAN」構築へ　仮想空間で通信網を模擬**
   メディア名📰：ケータイ Watch（2026年6月23日）
   ケータイ Watch | https://k-tai.watch.impress.co.jp/docs/news/2119381.html
   • KDDI、KDDI総合研究所、NVIDIA、Keysight Technologies、サムスンの5社が、実際の通信網を仮想空間に再現する「デジタルツインRAN」構築に向けた協業を発表。
   • AIによるネットワーク最適化・自律運用・新機能評価を、実網に影響を与えることなく安全かつ効率的に検証できる基盤の実現を目指す。
   • 役割分担はKDDIが商用網データ提供、KDDI総合研究所が電波伝搬予測技術、NVIDIAがデジタルツイン基盤（AODT）、Keysightが端末再現技術、サムスンがvRAN技術を担当する。

## 📰 業界・一般メディア（英語）

🔺 **Nvidia rallies telcos around AI agents at DTW Ignite**
   メディア名📰：Mobile World Live（2026年6月23日）
   Mobile World Live | https://www.mobileworldlive.com/nvidia/nvidia-rally-telcos-around-ai-agents-at-dtw-ignite/
   • NVIDIAがDTW Ignite 2026（コペンハーゲン開催）にて、SoftBank・NTT DATA・KDDI等の通信事業者とともに、タスクベースの自動化から完全自律型ネットワーク運用への移行を支援する「テレコムAIエージェント」技術スタックを実演。
   • SoftBankはNVIDIA NeMo Safe Synthesizer／NeMo Anonymizerを用いてプライバシー保護型の合成データを生成し、自社の大規模テレコムモデル（LTM）の微調整・専用ネットワークエージェント構築に活用している。
   • KDDIはNVIDIA・Keysight・Samsung Research Americaと共同で6G向けRANデジタルツイン構築を進めるなど、シミュレーション・エージェントランタイム分野で複数企業が新たな協業を発表した。

---
*このDigestはAI RANウォッチャーが自動生成しています。*
