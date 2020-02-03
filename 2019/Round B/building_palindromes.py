from collections import Counter

def is_palindrome(string, start, end):
    char_counts = Counter(string[start:end])
    n_odd_counts = 0
    for char in char_counts:
        if char_counts[char] % 2 == 1:
            n_odd_counts += 1
        if n_odd_counts > 1:
            return False
    return True

T = int(input())
for x in range(1, T+1):
    N, Q = map(int, input().split())
    string = input()
    dict_ = {}
    n = 0   # number of yes
    for _ in range(Q):
        l, r = map(int, input().split())
        if (l, r) not in dict_:
            dict_[(l,r)] = is_palindrome(string, l-1 ,r)
        if dict_[(l,r)]:
            n += 1
    print("Case #{}: {}".format(x, n))