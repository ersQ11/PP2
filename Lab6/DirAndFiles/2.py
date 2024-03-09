import os

def check_access(path):
    if os.access(path, os.F_OK):
        print(f"Path '{path}' exists.")
    else:
        print(f"Path '{path}' does not exist.")

    if os.access(path, os.R_OK):
        print(f"Path '{path}' is readable.")
    else:
        print(f"Path '{path}' is not readable.")

    if os.access(path, os.W_OK):
        print(f"Path '{path}' is writable.")
    else:
        print(f"Path '{path}' is not writable.")

    if os.access(path, os.X_OK):
        print(f"Path '{path}' is executable.")
    else:
        print(f"Path '{path}' is not executable.")

specified_path = "C:\PP2\Lab6\DirAndFiles"
check_access(specified_path)
