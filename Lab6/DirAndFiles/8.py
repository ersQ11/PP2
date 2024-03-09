import os

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.R_OK):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"Error: No read permissions for file '{file_path}'.")
        else:
            print(f"Error: File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {str(e)}")

specified_path = "C:\PP2\Lab6\DirAndFiles\\test.txt"
delete_file(specified_path)
