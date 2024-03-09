import os

def write_list_to_file(file_path, my_list):
    """
    Writes a list to a text file using the os module.
    """
    try:
        with open(file_path, 'w') as file:
            for item in my_list:
                file.write(f"{item}\n")
        print(f"List written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {str(e)}")

# Example usage:
my_list = ['Geeks', 'for', 'Geeks!']
file_path = "my_list2.txt"
write_list_to_file(file_path, my_list)
