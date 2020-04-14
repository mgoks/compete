'''Whenever it finds a card that is lexicographically smaller than the previous 
card, it moves that card to its correct place in the stack above.'''
def robot_sort(A):
    n = 0       # number of swaps
    max_ = A[0] # max element of sorted stack above
    for i in range(1, len(A)):  # keeping track of max...
        cur = A[i]
        if cur > max_:  # no swap needed
            max_ = cur  # just expand the sorted stack by updating max
        else:       # cur < max, 
            n += 1  # put cur in its correct position by swapping
    return n

T = int(input())
for x in range(1, T+1):
    N = int(input())
    names = [input() for _ in range(N)]
    print("Case #{}: {}".format(x, robot_sort(names)))