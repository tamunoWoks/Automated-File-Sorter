# Automated File Sorter
This Python script automates the organization of files within a specified directory by sorting them into folders based on file types. It runs continuously, performing the sorting process every 3 hours, allowing users to keep their directories neat and organized effortlessly.

## Features
- Automated Sorting: Files are moved to specific folders based on their file extensions.
- Scheduled Execution: The script runs every 3 hours to ensure that new files are sorted regularly.
- Configurable Folders: The script can be easily modified to include more file types and folders as needed.
- Cross-Platform Support: Uses os.path.join to ensure paths are compatible across operating systems.

## Notes
- The script skips items that are not files (e.g., folders) and files with unrecognized extensions.
- This script will run indefinitely, so it’s recommended to execute it in an environment that allows continuous running, such as a background process or task scheduler.

## Folder Structure
The script sorts files into the following folders by default:

- csv files: For .csv files
- image files: For .png files
- text files: For .txt files  

If additional file types need to be sorted, users can add new folder mappings by modifying the folder_mappings dictionary in the script.

## Requirements
- Python 3.6 or higher
- Required modules: os, shutil, time (all included in the Python standard library)

## Code Overview
- folder_mappings Dictionary: Maps file extensions to corresponding folder names.
- Folder Creation: Creates folders for each file type if they don’t already exist.
- sort_files() Function:
  - Scans the directory and identifies files based on their extensions.
  - Moves each file to the corresponding folder based on the extension defined in folder_mappings.
  - Prints a message indicating the success or status of each move.
- 3-Hour Timer: The script pauses for 3 hours (time.sleep(3 * 60 * 60)) after each sorting cycle to ensure it runs periodically.
