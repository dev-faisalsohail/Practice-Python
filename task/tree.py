# Directory Tree Viewer

import os
import sys

def show_tree(path, prefix=""):
    items = os.listdir(path)
    for index, item in enumerate(items):
        full_path = os.path.join(path, item)
        connector = "└── " if index == len(items) - 1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if index == len(items) - 1 else "│   ")
            show_tree(full_path, new_prefix)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tree.py <directory_path>")
    else:
        directory = sys.argv[1]
        if os.path.exists(directory):
            print(directory)
            show_tree(directory)
        else:
            print("Path not found!")



import os
import shutil
from datetime import datetime

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(file)
            ext_folder = ext[1:].upper() if ext else "OTHERS"
            dest_folder = os.path.join(folder_path, ext_folder)
            os.makedirs(dest_folder, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_name = f"{name}_{timestamp}{ext}"
            new_path = os.path.join(dest_folder, new_name)

            shutil.move(file_path, new_path)
            print(f"Moved: {file} → {new_path}")

folder = input("Enter directory path to organize: ")
organize_files(folder)
