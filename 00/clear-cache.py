import os
import sys
import shutil


def clear_pycache(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for filename in filenames:
            if filename.endswith('.swp'):
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        for dirname in dirnames:
            if dirname == '__pycache__':
                full_path = os.path.join(dirpath, dirname)
                shutil.rmtree(full_path)
                print(f"Removed: {full_path}")


if __name__ == "__main__":
    assert len(sys.argv) <= 2, "too many arguments"
    root_directory = '.'
    if len(sys.argv) == 2:
        root_directory = sys.argv[1]
    clear_pycache(root_directory)

