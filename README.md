# NM-HELPER: Python CLI helper tool and terminal automation utility

NM-HELPER is a Python CLI helper tool and terminal automation utility that organizes and renames document files into student-specific PDF sets.

The terminal automation utility copies files from a source directory, generates individual recipient folders, and renames each file to match course naming conventions. This Python CLI helper tool runs locally in terminal environments such as Termux on Android.

## Architecture

Remane.py contains the entire logic using the Python standard library modules os and shutil.

1. Source directory scanning: The script reads all files in /storage/emulated/0/Nm with os.listdir.
2. Output directory creation: The script creates the base directory /storage/emulated/0/NM-final and individual subdirectories for each person with os.makedirs.
3. File copying: The rename function copies each file to the destination subdirectory with shutil.copy.
4. File renaming: The script renames each copied file to include the recipient name and the tag (CSBS).pdf with os.rename.

## Setup

NM-HELPER requires Python 3. The script relies on Python standard library modules and requires no external packages.

1. Clone the repository:
```bash
git clone https://github.com/devsanthoshmk/NM-HELPER.git
cd NM-HELPER
```

2. Verify the Python 3 installation:
```bash
python3 --version
```

3. Grant storage permissions in Termux:
```bash
termux-setup-storage
```

## Usage

1. Create the source folder /storage/emulated/0/Nm and place the target files inside it.
2. Run the script:
```bash
python3 Remane.py
```
3. Find the processed files in /storage/emulated/0/NM-final/<name>/.

## Configuration

You configure settings directly in Remane.py.

- Line 3 sets the source path in variable place. The default path is "/storage/emulated/0/Nm".
- Line 4 sets the destination path in variable dist by removing the last 2 characters from place and appending "NM-final".
- Line 16 specifies the target recipient list with 4 names: 'Santhosh M K ', 'Ranjith P', 'Prakash S', and 'Aman'.
- Line 12 defines the naming format by stripping the last 4 characters of the source filename and appending the suffix "-{name}(CSBS).pdf".
