import os
import shutil

def clear_pycache(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            if dirname == '__pycache__':
                full_path = os.path.join(dirpath, dirname)
                shutil.rmtree(full_path)
                print(f"Removed: {full_path}")

# Specify the root directory from which to start clearing __pycache__ directories
root_directory = '.'  # Use '.' for the current directory or specify another path
clear_pycache(root_directory)

