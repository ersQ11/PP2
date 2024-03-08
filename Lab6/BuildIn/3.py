def palindrome(w):
    palidrome_counter = 0
    for i in range (0, len(w)):
        if word_list [i] == word_list[(len(w)-1)-i]:
            palidrome_counter += 1
        else: pass
    if palidrome_counter == len(w):
        return True
    else: return False
    
word = input()
word_list = list(word)
print(palindrome(word_list))