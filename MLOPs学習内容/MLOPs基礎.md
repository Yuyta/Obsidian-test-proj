# MLOPsとは
MLOperations。AI運用し持続的にUpdateしていくための仕組み。
データ処理及び、モデルデプロイを円滑化。

# MLOPsのプロセス
①データ抽出
②データ分析
③データ準備
④モデルの訓練
⑤モデルの評価
⑥モデルの検証
⑦訓練済モデルの配置
⑧モデルの提供
⑨モデルのモニタリング

# MLOPsフレームワーク
## クラウド関連のフレームワーク
Google Vertex AI、Amazon SageMaker、Azure Machine Learning

## エンタープライズ向けベストプラクティス
Weights ＆ Biases(wandb)

## OSS
MLflow、Metaflow、Tensorflow、Extended

# MLflow環境構築
 - トラッキングサーバー
 - バックエンド
 - Artifactストレージ
 - レジストリサーバー

# 用語・利用する技術
- オフライン特徴量ストア：学習用に用いるストア。過去の大量データをためてモデルを育てる場所
- オンライン特徴量ストア：予測用に用いるストア。今この瞬間のデータをすぐに取り出して予測する場所
- DVC(Data Version Control)：データバージョン管理ツール。モデルをgitなどで追跡可能にする。
- Docker：
- FastAPI：
- CI/CD：
# 参考情報
[ハンズオン]([【ハンズオン】 Docker + MLflow + DVC で構築するMLOps入門 #Python - Qiita](https://qiita.com/tactac1238/items/a94c3553d3772d1e93d7))のリンクからMLOPsの基礎を学べる。