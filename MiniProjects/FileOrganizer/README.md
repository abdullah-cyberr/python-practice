# 📂 File Organizer v2.0

A Python project that automatically organizes files into categorized folders based on their file extensions.

## Features

- Organizes files automatically
- Supports Images, Documents, Music, Videos, Archives, Executables, Python Files, and Data
- Unknown file types are moved to the **Others** folder
- Professional Summary Report
- Logging system (`organizer.log`)
- Exception Handling
- Configurable default folder
- Command-line argument support

## Technologies Used

- Python 3
- pathlib
- shutil
- logging
- sys

## How to Run

### Default Folder

```bash
py organizer.py
```

### Custom Folder

```bash
py organizer.py "D:\MyFolder"
```

## Example Output

```text
========================================
      FILE ORGANIZER v2.0
========================================
Scanning Folder: TestFolder

Files Organized: 5

========== SUMMARY ==========
Images         : 2
Documents      : 1
Music          : 1
Others         : 1
----------------------------
Total Files    : 5
============================
```

## Project Structure

```text
FileOrganizer/
│── organizer.py
│── organizer.log
│── README.md
└── TestFolder/
```

## Author

Rakib