import re

input_string = input()

a = re.sub(r'[''"" .]{1}', ":", input_string)

print(a)

'''pattern = re.compile(r'[''"" .]+')
matches = pattern.finditer(input_string)
for match in matches:
    re.sub(pattern, ":", match)
print(input_string)'''