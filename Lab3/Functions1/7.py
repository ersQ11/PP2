def has_33(nums):
    for i in range(1, len(nums)-1):
        if number_list[i] == 3:
            if number_list[i+1] == number_list[i] or number_list[i-1] == number_list[i]:
                return False
            else:
                return True
    

numbers = input()
number_list = list(int(x) for x in numbers.split())
print(has_33(number_list))
