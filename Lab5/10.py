import re

def insert_spaces(str):
    result = re.sub(r'([a-z])([A-Z])', r'\1_\2', str)
    return result

input_string = input()
print(insert_spaces(input_string))