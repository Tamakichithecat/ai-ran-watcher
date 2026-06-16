# 📡 AI RAN Digest — 2026-06-16

収集日時: 2026-06-16 09:00 JST | 新規記事: 6件
🔴標準化:1　📄論文:0　🏢企業:2　🇯🇵国内:0　📰海外:3

---

## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）

🔺 **6G Standardization Key Milestones and RAN Decisions**
   Ericsson | https://www.ericsson.com/en/blog/2026/6/6g-standardization-key-milestones-and-ran-decisions
   • 2026年6月のプレナリーで6G（IMT-2030）向けキー技術スタディのチェックポイントを迎え、3GPP Rel-21タイムラインの正式合意が行われた。
   • 6Gの最初のRadio Study期間（〜2027年6月）においてAI/ML-nativeなRAN設計が重点課題として位置付けられている。
   • 高レイヤースプリット（CU/DU分割）は5Gと同等のアーキテクチャが採用方針として合意済みで、AI-RAN機能の段階的組み込みが標準化の主軸となっている。

---

## 📄 論文・技術文書（IEEE Xplore等）

（本収集期間に新規URLなし）

---

## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank / Ericsson 等）

🔺 **NVIDIA and US Telecom Leaders Unveil the All-American AI-RAN Stack to Accelerate the Path to 6G**
   企業名🏢：NVIDIA / Booz Allen / Cisco / MITRE / ODC / T-Mobile
   NVIDIA Newsroom | https://nvidianews.nvidia.com/news/nvidia-us-telecom-ai-ran-6g
   • NVIDIAと米国通信大手が米国初のAI-native 6Gワイヤレススタックを構築し、NVIDIA AI Aerialプラットフォーム上でAI-WIN初のユーザー間通話を実施。
   • Multimodal ISAC（映像＋RF融合センシング）とAIによるスペクトル・アジリティ制御という先進6Gアプリケーションを実証。7倍のセル容量・3.5倍の電力効率を達成（Cerberus ODC社比）。
   • NVIDIA Aerial Frameworkによりサードパーティアプリが物理レイヤーデータにAPIアクセス可能となり、AI-RANスタック上での6Gアプリエコシステム形成を促進。

・ **SoftBank Corp. and Ericsson to Deploy AI-Powered External Control System to Optimize Massive MIMO Coverage**
   企業名🏢：SoftBank / Ericsson
   Ericsson Newsroom | https://www.ericsson.com/en/press-releases/2/2026/softbank-and-ericsson-to-deploy-ai-powered-external-control-system-to-optimize-massive-mimo-coverage
   • SoftBankとEricssonが東京圏の大規模会場向けにMassive MIMO向けAI外部制御カバレッジ最適化システムを商用展開開始。
   • Expo 2025大阪での商用トライアルにて5G下り方向スループットが約24%向上することを確認済み。AIがトラフィック変動に応じてビームパターンを自律制御。
   • 2026年中に複数の大型アリーナ・ドーム施設へ順次展開予定。既存Massive MIMO設備へのソフトウェア追加で実現可能な構成。

---

## 🇯🇵 日本語メディア

（本収集期間に該当する新規記事なし）

---

## 📰 業界・一般メディア（英語）

🔺 **Nvidia Has a Radical New AI-RAN Plan – a 6G Radio Unit Chip**
   メディア名📰：Light Reading
   Light Reading | https://www.lightreading.com/6g/nvidia-has-a-radical-new-ai-ran-plan-a-6g-radio-unit-chip
   • NVIDIAが6G Radio Unit（RU）内部に搭載するGPUチップを開発中との報道（2026年6月8日）。従来のCU/DU（基地局コンピュート）に留まらずアンテナ直下のRUにまでGPU展開を拡大する方向性。
   • Ultra-MIMO（6G高周波帯で最大1,024T×R想定）においては低PHY処理の計算量が5Gの32倍超となり、RUへのGPU搭載が「必須」になるとNVIDIAは表明。ただし製品開発を正式確認はしていない。
   • Marvell（Octeon BSPをNVIDIA GPUと統合予定）やNokia・Ericssonのシリコン戦略に直接影響する業界再編の予兆として注目される。

🔺 **Analysis: Nvidia's Rumored New 6G AI-RAN – Likely Features/Functions and Industry Impact**
   メディア名📰：IEEE ComSoc Technology Blog
   IEEE ComSoc Tech Blog | https://techblog.comsoc.org/2026/06/09/analysis-nvidias-rumored-new-6g-ai-ran-likely-features-functions-and-industry-impact/
   • IEEE ComSoc執筆のシナリオ分析（2026年6月9日）。NVIDIA製6G RU向けGPUが搭載すると想定されるAI機能として、ニューラル・チャネル推定、リアルタイム・ビーム管理、スペクトル・アジリティ、エッジ推論フックなどを詳細解説。
   • 競合への影響分析：QualcommとMarvellがシリコン層で最大のリスクを受け、EricssonはRAN設計パラダイム転換の脅威、Nokiaは協業関係でリスク分散済みと評価。
   • 6G/IMT-2030のRITは2030年末まで確定しないため、本格的なシリコン設計完成は2031年以降になるとの技術的注意点も明記。

・ **Current 6G Trajectory is Evolutionary, According to Dell'Oro Group**
   メディア名📰：Dell'Oro Group
   Dell'Oro Group | https://www.delloro.com/news/current-6g-trajectory-is-evolutionary/
   • Dell'Oro（2026年6月11日）が6G RANの累積設備投資額は2034年までに5,000億ドルを超えると予測。ただし6Gは全体RANマーケットを拡大せず、2030〜2034年のCAGRは1%程度と試算。
   • 6Gは初期商用展開からAIをRANにネイティブ統合する設計となり、Sub-7GHzとcmWaveが主要周波数帯として機能する見通し。7GHz超のmmWave帯も段階的に加速する見込み。

---
*このDigestはAI RANウォッチャーが自動生成しています。*
