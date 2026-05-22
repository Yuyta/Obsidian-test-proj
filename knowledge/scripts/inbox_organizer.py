from pathlib import Path
import shutil
from datetime import datetime

def organize_inbox():
    # スクリプトの場所を基準にVaultのルートフォルダを特定
    script_dir = Path(__file__).resolve().parent
    vault_root = script_dir.parents[1]  # 2つ上の親ディレクトリ
    
    inbox_dir = vault_root / "knowledge" / "inbox"
    archive_dir = vault_root / "knowledge" / "archive"
    
    if not inbox_dir.exists():
        print(f"Inbox directory does not exist: {inbox_dir}")
        return
        
    # inboxの中のサブフォルダをスキャン
    for sub_dir in inbox_dir.iterdir():
        if not sub_dir.is_dir():
            continue
            
        # 移動先フォルダを特定（例: knowledge/archive/chatgpt/）
        target_archive_dir = archive_dir / sub_dir.name
        
        # サブフォルダ内のファイルをスキャン
        for file_path in sub_dir.iterdir():
            # ディレクトリはスキップし、ファイルのみを対象とする
            if not file_path.is_file():
                continue
                
            # 移動先フォルダを作成
            if not target_archive_dir.exists():
                try:
                    target_archive_dir.mkdir(parents=True, exist_ok=True)
                    print(f"Created archive directory: {target_archive_dir}")
                except OSError as e:
                    print(f"Failed to create directory {target_archive_dir}: {e}")
                    continue
                
            dest_path = target_archive_dir / file_path.name
            
            # 重複回避ロジック
            if dest_path.exists():
                base = dest_path.stem
                ext = dest_path.suffix
                # マイクロ秒まで含めて衝突を軽減
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                dest_path = target_archive_dir / f"{base}_{timestamp}{ext}"
                
                # 同一時刻で衝突する場合の最終チェック
                counter = 1
                while dest_path.exists():
                    dest_path = target_archive_dir / f"{base}_{timestamp}_{counter}{ext}"
                    counter += 1
                print(f"File conflict detected. Renamed to: {dest_path.name}")
                
            try:
                # shutil.move は str 型のパスを要求するため変換
                shutil.move(str(file_path), str(dest_path))
                print(f"Moved: {file_path.name} -> {dest_path.relative_to(vault_root)}")
            except PermissionError as e:
                print(f"Permission denied for {file_path.name}: {e}")
            except OSError as e:
                print(f"OS error occurred while moving {file_path.name}: {e}")
            except Exception as e:
                print(f"Unexpected error moving {file_path.name}: {e}")

if __name__ == "__main__":
    organize_inbox()
