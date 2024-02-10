def spy_game(nums):
    zero_count = 0
    seven_count = 0
    for i in range(0, len(nums)):
        if number_list[i] == 0:
            zero_count += 1
        elif number_list[i] == 7:
            seven_count += 1
    if zero_count >= 2 and seven_count >= 1:
        return True
    else: 
        return False

numbers = input()
number_list = list(int(x) for x in numbers.split())
print(spy_game(number_list))