# 📡 AI RAN Digest — 2026-08-30

収集日時: 2026-08-30 14:52 JST | 新規記事: 6件
🔴標準化:1　📄論文:2　🏢企業:1　🇯🇵国内:1　📰海外:1

## 🔴 標準化動向（3GPP / O-RAN / AI RAN Alliance / ITU / ETSI）

🔺 **3GPP RAN Working Groups Convene in Maastricht, TSG CT/SA Meet in Prague**
   whatthespec.net | https://whatthespec.net/3gpp/meeting/60713-3gppran1-126
   • 2026年8月24日〜28日、3GPPのRANワーキンググループ（RAN1#126、RAN2#135、RAN3#133、RAN4#120、RAN5#112）がオランダ・マーストリヒトで開催。RAN1だけで1,279名が登録し、1,744件の寄書が提出された。並行してTSG CT/SAはプラハで開催。
   • 各WGはRelease 19機能の保守作業に加え、Release 20のノーマティブ化作業を推進。同時に6GR（6Gラジオ）スタディアイテムの検討も継続され、AIネイティブな6Gアーキテクチャの標準化に向けた土台作りが進んだ。
   • 標準化はまだスタディフェーズが中心だが、次回会合（RAN1#126-bisは10月12日開催予定）に向けた重要な節目となった。

## 📄 論文・技術文書（IEEE Xplore等）

🔺 **Rethinking the Foundations of Two-Sided AI Models for 6G**
   著者😎：Yongjeong Oh, Zihan Chen, Timothy J. O'Shea, Junyong Shin, Jinho Choi, Yo-Seb Jeon, Jihong Park
   arXiv | https://arxiv.org/abs/2608.22918
   • 送受信機の両側にAIモデルを配置する「Two-Sided AIモデル」について、チャネルフィードバックとデータ通信の効率化を目的に基礎から再検討。2026年8月24日にarXivへ投稿。
   • レガシー端末との共存、事前定義されたチャネル条件下での学習、ベンダー間通信を要する勾配ベースの微調整といった実装上の課題を整理し、実用的な代替手法を提示。
   • 5G NRのプロトコルスタックにTwo-Sidedモデル処理を統合し、実機テストベッドでレガシーNR方式との共存動作を検証した点が特徴。

・ **Test-Time Scalable AI-RAN: Inference Time Allocation for Cell-Free MIMO**
   著者😎：Seonghoon Yoo, Joonhyuk Kang（KAIST）, Sangwoo Park（King's College London）, Seok-Hwan Park（Hanyang University ERICA）
   arXiv | https://arxiv.org/abs/2608.03614
   • LLMで注目された「テストタイムスケーラビリティ」（推論時に計算資源を追加投入するほど性能が向上する性質）を、セルフリーMIMO方式のAI-RANシステムに応用した研究。
   • 各AIモジュールに割り当てる追加計算資源量を、他モジュールおよび無線チャネルとの相互作用を踏まえて最適化する汎用フレームワークを提案。
   • セルフリー大規模MIMO環境でのAI-RAN実装における性能・効率向上に資する内容で、KAISTなど3大学の研究者が共同執筆。

## 🏢 企業プレスリリース（NVIDIA / T-Mobile / SoftBank）

🔺 **SoftBank and Ericsson Verify AI-Native Link Adaptation Scheduler on Commercial 5G Network**
   企業名🏢：SoftBank Corp / Ericsson Japan
   SoftBank Corp | https://www.softbank.jp/corp/news/press/sbkk/2026/20260820_02/
   • ソフトバンクとエリクソン・ジャパンは2026年8月20日、エリクソンの「AI in RAN」に含まれるAIネイティブ・リンクアダプテーション用スケジューラーを、ソフトバンクの5G商用ネットワークで実証したと発表。RAN内部にAIを直接組み込みリアルタイムに動作させる手法を国内で初めて検証した。
   • 従来技術と比較し、スペクトル効率が最大約25％、下りユーザースループットが最大約50％向上。全評価エリアの平均でもスペクトル効率・下りスループットともに約10％の改善を確認した。
   • 両社は5G-Advancedおよび将来の6Gに向けて協業を継続し、AIネイティブなRANソフトウエアの進化を目指す方針。

## 🇯🇵 日本語メディア

🔺 **エヌビディア製GPUは6Gに必須か？ノキアのAI-RAN戦略にエリクソンとサムスンが異論**
   メディア名📰：財経新聞
   財経新聞 | https://www.zaikei.co.jp/article/20260828/867821.html
   • ノキアがNVIDIA製GPUを6G基地局の必須要素と位置付ける一方、エリクソンとサムスンはGPU必須論に異論を唱えていると報じた記事。RAN大手3社の技術戦略の違いを整理している。
   • ノキアは2025年にNVIDIAから10億ドルの出資を受け入れ、CUDAベースのRANソフトウエア開発と、将来製品でのMarvell製カスタムシリコンからの全面移行を表明済み。
   • エリクソンは送信時間間隔（TTI、約500マイクロ秒）などRAN特有の制約から軽量AIモデルで十分と主張し、専用シリコン（カスタムASIC）戦略の継続を強調している。

## 📰 業界・一般メディア（英語）

🔺 **Ericsson, Nokia and Samsung Clash Over 6G's Need for Nvidia**
   メディア名📰：Light Reading
   Light Reading | https://www.lightreading.com/6g/ericsson-nokia-and-samsung-clash-over-6g-s-need-for-nvidia
   • ノキアCTOのPallavi Mahajan氏は、GPU活用によりRKHS（再生核ヒルベルト空間）のような計算負荷の高いアルゴリズムが実行可能になるとし、2028年までにスペクトル効率を最大2倍にできると主張。既存のAirscale筐体に挿入可能なGPUカードも投入予定。
   • エリクソンは「GPUは6G/AI-RANの選択肢の一つに過ぎない」と反論。TTI（送信時間間隔、約500マイクロ秒）の制約上、AIモデルは数万パラメータ規模に軽量化する必要があり、専用シリコンで十分と説明。神経網アクセラレータをMassive MIMO無線機に搭載する戦略を推進。
   • サムスンもGPU必須論には否定的で、CPUを汎用基盤としつつ必要な処理にのみGPU等のアクセラレータを追加する方針。CPUをSUV、GPUをスポーツカーに例え、RAN大手3社の技術戦略の分岐が鮮明になっていると報じている。

---
*本日はRAWデータソースからの新規記事収集が0件だったため、全記事をWeb検索による補完調査で収集しました。2026年8月24日〜28日に3GPP RAN/CT/SAワーキンググループ会合がマーストリヒト・プラハで開催され、Release 20の仕上げと6Gスタディの双方が進展しました。また、ノキア・エリクソン・サムスンの間でAI-RANにおけるGPU活用の是非を巡る技術戦略の対立が鮮明になっており、今後の6G基地局アーキテクチャの方向性を占う焦点として注目されます。*
