from collections import namedtuple

Activity = namedtuple('Activity', 'start, end, index')

for t in range(1, int(input()) + 1):
    N = int(input())
    
    acts, schedule = [], [''] * N
    for i in range(N):
        s, e = tuple(map(int, input().split()))
        acts.append(Activity(s, e, i))

    acts.sort()
    c_end, j_end = 0, 0
    for start, end, i in acts:
        if c_end <= start:
            c_end, schedule[i] = end, 'C'
        elif j_end <= start:
            j_end, schedule[i] = end, 'J'
        else:
            schedule = ['IMPOSSIBLE']
            break
    print('Case #{}: {}'.format(t, ''.join(schedule)))
