import re

input_string = input()

pattern = re.compile(r"([a-z]+_*?)")
matches = pattern.finditer(input_string)
for match in matches:
    print(match)