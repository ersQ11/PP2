import re

input_string = input()

pattern = re.compile(r'[A-Z]{1}[a-z]+')
matches = pattern.finditer(input_string)
for match in matches:
    print(match)