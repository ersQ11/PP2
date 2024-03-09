import os

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

path = "test.txt"
count_lines_in_file(path)
