---
title: action-with-visual-primitives-avp
authors: 
year: 
source: 
---

---
title: action-with-visual-primitives-avp
authors: 
year: 
source: 
---

---
title: action-with-visual-primitives-avp
authors: 
year: 
source: 
---

---
title: Action with Visual Primitives（AVP）: 視覚プリミティブを用いた行動生成
authors: Weilong Guo 他
year: 2026
source: knowledge/archive/academic_papers/Action_with_Visual_Primitives.md
tags: [VLA, ロボティクス, マルチモーダル]
---

概要:
Vision-Language-Actionモデルにおける指示解釈、視覚理解、運動制御を単一の学習目標でまとめる従来設計の問題を指摘し、VLMが出力する「視覚プリミティブ」トークンをアクション専門家（flow-matching action expert）に条件付けする二段構成のAVPアーキテクチャを提案する。実ロボットのピック＆プレース課題で成功率が大きく改善し、データ効率、空間的組合せ一般化、オブジェクトレベルの転移性能も向上した。

方法:
- VLM: 次段階ターゲットを推論し、視覚プリミティブを生成
- Action expert: 視覚プリミティブを条件にしてflow-matchingで運動を生成
- 教師信号: エンドエフェクタのキネマティクスに由来

結果:
- ベースライン比で成功率が約27.6%向上
- データ効率と一般化性能の一貫した向上を報告

示唆:
- ロボット操作タスクでの“認知（理解）”と“制御（運動）”の明確な分離は学習効率と転移性を高める。

制限:
- タスクは主にピック＆プレースに集中。より複雑な操作や多段階タスクでの検証が必要。

## 関連ファイル
- [[Action_with_Visual_Primitives]]
- [ソースファイル](../archive/academic_papers/Action_with_Visual_Primitives.md)
