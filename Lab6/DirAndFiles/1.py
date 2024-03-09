import os

def directories_and_files(path):

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"Directory: {item_path}")
        elif os.path.isfile(item_path):
            print(f"File: {item_path}")

specified_path = "C:\PP2\Lab6\DirAndFiles"
directories_and_files(specified_path)

