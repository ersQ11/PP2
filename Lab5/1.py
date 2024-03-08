import re

input_string = input()

pattern = re.compile(r'ab*')
matches = pattern.finditer(input_string)
for match in matches:
    print(match)