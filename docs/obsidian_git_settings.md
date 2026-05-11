# Obsidian Git 推奨設定ガイド (2026年版)

このドキュメントは、論文調査自動化ワークフローを安全かつ効率的に運用するための、Obsidian Gitプラグインの設定指針をまとめたものです。

## 概要
GitHub Actionsによる外部からの論文追加を自動で受け取りつつ、自身のメモ作成を妨げない同期設定を定義します。

## 設定一覧

### 1. 自動同期設定 (Auto Sync)
| 項目名 | 設定値 | 備考 |
| :--- | :--- | :--- |
| **Auto commit-and-sync interval** | `15` | 15分おきに同期を試行。 |
| **Auto commit-and-sync after stopping file edits** | **ON** | 執筆停止5分後に同期（入力中のカクつきを防止）。 |
| **Auto pull interval** | `0` | `commit-and-sync` に含まれるため不要。 |

### 2. 同期・Pull設定 (Pull & Sync)
| 項目名 | 設定値 | 備考 |
| :--- | :--- | :--- |
| **Pull on startup** | **ON** | **重要。** 起動時に最新の調査結果を取得します。 |
| **Merge strategy** | **Merge** | 競合を安全に解決するための標準設定。 |
| **Push on commit-and-sync** | **ON** | 自身のメモをGitHubへバックアップします。 |
| **Pull on commit-and-sync** | **ON** | 同期時に常に最新の状態を確認します。 |

### 3. 表示・通知設定 (Display & Notification)
| 項目名 | 設定値 | 備考 |
| :--- | :--- | :--- |
| **Disable informative notifications** | **ON** | 成功時の通知を非表示にして作業に集中。 |
| **Disable error notifications** | **OFF** | エラー（認証切れ等）には気づけるようにします。 |
| **Hide notifications for no changes** | **ON** | 変更がない時の不要な通知をカット。 |
| **Show status bar** | **ON** | 同期状態を画面下部で確認可能にします。 |

### 4. 作成者情報 (Author Information)
| 項目名 | 設定値 |
| :--- | :--- |
| **Author name** | あなたのGitHubユーザー名 |
| **Author email** | GitHub登録メールアドレス |

---

## 運用上の注意
- **競合の回避**: `knowledge/inbox/academic_papers/` フォルダ内のファイルはGitHub Actionsによる自動収集の対象です。これらのファイルを編集・整理する際は、`knowledge/research/` 配下の適切なフォルダへ移動させてから行うことを推奨します。
- **インプットの集約**: ChatGPTやGeminiからの調査結果を `knowledge/inbox/chatgpt/` 等に追加した際も、定期的に同期（Sync）が実行され、GitHub上でバックアップされます。
- **複数デバイス**: すべてのデバイスで同じ **Author name/email** を設定し、コンフリクトを最小限に抑えてください。
