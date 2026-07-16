import shutil
from pathlib import Path

# যে folder organize করব
folder = Path("TestFolder")

# File Type Mapping
file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".exe": "Executables",
    ".zip": "Archives",
    ".csv": "Data",
    ".py": "Python Files"
}

# সব file scan করো
for file in folder.iterdir():

    # Folder skip করো
    if file.is_file():

        extension = file.suffix

        # Extension dictionary-তে থাকলে
        if extension in file_types:

            category = file_types[extension]

            # Category folder তৈরি করো
            category_folder = folder / category
            category_folder.mkdir(exist_ok=True)

            # Destination তৈরি করো
            destination = category_folder / file.name

            # File move করো
            shutil.move(file, destination)

            print(f"Moved: {file.name} -> {category}")