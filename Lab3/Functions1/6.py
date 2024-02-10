def reverse(x):
    for i in range (0, len(x)):
        string_list [i] = string_list[(len(x)-1)-i]
        reverse_list.append("".join(string_list[i]))

    print(" ".join(reverse_list))

strin = input()
string_list = list(strin.split())
reverse_list = []
reverse(string_list)