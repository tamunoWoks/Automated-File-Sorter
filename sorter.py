# Import necessary modules
import os, shutil, time

# Define the path
path = r"C:/Users/ADMIN/Documents/Python/File sorter/"

# Define file extensions and their corresponding folders
folder_mappings = {
    '.csv': 'csv files',
    '.png': 'image files',
    '.txt': 'text files'
}

# Create folders if they do not exist
for folder in folder_mappings.values():
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
