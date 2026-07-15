from pathlib import Path

folder = Path("cyberLogs")

if not folder.exists():
    folder.mkdir()
    print("Folder Created")

else:
    print("Folder Already Exists")