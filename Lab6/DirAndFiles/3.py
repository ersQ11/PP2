import os

def check_path(path):

    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"Path '{path}' does not exist.")

specified_path = "C:\PP2\Lab6\DirAndFiles"
check_path(specified_path)
