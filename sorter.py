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

# Function to sort files
def sort_files():
    # List all items in the directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # Only process if it's a file
        if os.path.isfile(item_path):
            # Check the file extension and move to the corresponding folder
            file_ext = os.path.splitext(item)[1]
            if file_ext in folder_mappings:
                dest_folder = os.path.join(path, folder_mappings[file_ext])
                shutil.move(item_path, os.path.join(dest_folder, item))
                print(f"Moved: {item} to {folder_mappings[file_ext]}")
            else:
                print(f"Skipped (no matching folder): {item}")

# Run the sort_files function every 3 hours
while True:
    sort_files()
    print("Files sorted. Next sort in 3 hours.")
    # Wait for 3 hours (3 * 60 * 60 seconds)
    time.sleep(3 * 60 * 60)
