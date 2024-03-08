import re

def snake_to_camel(snake_str):
    temp = re.split('_+', snake_str)
    res = temp[0] + ''.join(map(lambda x: x.title(), temp[1:]))
    return res

input_string = input()

print(snake_to_camel(input_string))



