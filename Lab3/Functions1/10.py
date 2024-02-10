def uniq(nums):
    for i in range(0, len(nums)):
        if number_list[i] not in unique:
            unique.append(number_list[i])
        else: pass
    print(unique)

numbers = input()
number_list = list(int(x) for x in numbers.split())
unique = []
uniq(number_list)
