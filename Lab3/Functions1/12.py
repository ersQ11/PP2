def histogram(x):
    for i in range(0, len(x)):
        while x[i] > 0:
            star_list.append("".join("*"))
            x[i] -= 1
        print("".join(star_list))
        star_list.clear()

nums = input()
numbers = list(int(x) for x in nums.split())
star_list = []
histogram(numbers)
