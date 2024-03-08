import re

def split_to_letters(string):
    letters = re.findall(r'[a-zA-Z]', string)
    Letters = [x.upper() for x in letters]
    return Letters


input_string = input()
result = split_to_letters(input_string)
print(result)
