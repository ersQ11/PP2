import itertools

def permu(k):
    perms = itertools.permutations(k)
    for t in perms:
        print("".join(t))
        
k = input()
permu(k)