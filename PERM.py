import math
from itertools import permutations

def all_permutations(n):
    nums = list(range(1, n+1))
    perms = permutations(nums)
    return list(perms)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    perms = all_permutations(n)
    print(math.factorial(n))
    for p in perms:
        print(' '.join(map(str, p)))
