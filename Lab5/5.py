import re

input_string = input()

pattern = re.compile(r'a.*b\b')
matches = pattern.finditer(input_string)
for match in matches:
    print(match)