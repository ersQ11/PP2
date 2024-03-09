import os

def write_list_to_file(file_path, my_list):
    with open(file_path, 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")
    print(f"List written to '{file_path}' successfully.")

my_list = ("Kbtu", "hello", "everyone")
file_path = "my_list.txt"
write_list_to_file(file_path, my_list)
