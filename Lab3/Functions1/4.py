def filter_prime(n):
    if n < 2:
        return 0
    for i in range (2, int((n**0.5) + 1)):
        if n % i == 0:
            return 0
    return 1

nums = input("Numbers: ")
numbers = [int(x) for x in nums.split()]
numbers.sort()
prime_numbers = list(filter(filter_prime, numbers))

print("Prime numbers:", prime_numbers)