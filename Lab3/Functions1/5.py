def generate_permutations(input_string):
    """
    Generates all permutations of the input string.

    Args:
        input_string (str): The input string for which permutations are to be generated.

    Returns:
        list: A list of all permutations of the input string.
    """
    def backtrack(start):
        if start == len(input_string):
            all_permutations.append("".join(input_string))
            return
        for i in range(start, len(input_string)):
            input_string[start], input_string[i] = input_string[i], input_string[start]
            backtrack(start + 1)
            input_string[start], input_string[i] = input_string[i], input_string[start]

    all_permutations = []
    input_string = list(input_string)  # Convert input string to a list for easier swapping
    backtrack(0)
    return all_permutations

# Example usage:
user_input = input("Enter a string: ")
permutations = generate_permutations(user_input)
print("All permutations of the input string:")
for perm in permutations:
    print(perm)
