import os

def generate_alphabet_files():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    directory = 'letters'

    if not os.path.exists(directory):
        os.makedirs(directory)

    for letter in alphabet:
        file_path = os.path.join(directory, f"{letter}.txt")
        with open(file_path, 'w') as file:
            file.write(letter)

        print(f"File '{file_path}' created.")

generate_alphabet_files()
