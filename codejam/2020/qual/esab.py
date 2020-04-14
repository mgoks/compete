from sys import stdout

def query(i):
    global query_num
    query_num += 1
    print(i+1)
    stdout.flush()
    return int(input())

def flip(ans):
    for i, bit in enumerate(ans):
        if bit > -1:
            ans[i] ^= 1


T, B = map(int, input().split())
for _ in range(T):
    ans = [-1] * B
    s = d = -1  # same pair, diff pair indices
    query_num = 1
    for i in range(B//2):
        if query_num > 1 and query_num % 10 == 1:
            if s > -1 and d > -1:
                same, diff = query(s), query(d)
                if same != ans[s] and diff != ans[d]:
                    flip(ans)
                elif same != ans[s]:
                    ans.reverse()
                    flip(ans)
                elif diff != ans[d]:
                    ans.reverse()
            elif s > -1:
                if query(s) != ans[s]:
                    flip(ans)
                query(s)
            elif d > -1:
                if query(d) != ans[d]:
                    flip(ans)
                query(d)
        j = B-1-i
        ans[i], ans[j] = query(i), query(j)
        if ans[i] == ans[j]:
            s = i
        else:
            d = i
    print(''.join(str(bit) for bit in ans))
    stdout.flush()
    input()
