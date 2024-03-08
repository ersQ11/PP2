nums = input()
numbers = list(int(x) for x in nums.split())
n = int(input())

nums_multiple = list(map(lambda x: x * n, numbers))

print(nums_multiple)