def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for letter in string:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    return upper_count, lower_count

# Пример использования:
input_string = input()
upper, lower = count_upper_lower(input_string)
print("Upper case:", upper)
print("Lower case:", lower)
