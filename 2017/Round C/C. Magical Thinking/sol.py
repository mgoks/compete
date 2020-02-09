for case_no in range(1, int(input()) + 1):
    '''
    Each begins with one line with two integers N and Q. Then, N+1 lines follow;
    the i-th of these lines represents the i-th examinee's list of answers Ai, 
    and has Q characters, each of which is either T or F (representing True or 
    False). AN+1 is your own list of answers. Finally, one line with N integers 
    follows; the i-th of these integers, Si, represents the i-th examinee's 
    score. (Note that your own score is not in this list, because it is 
    unknown.)

    n ... number of friends
    q ... number of questions
    '''
    n, q = map(int, input().split())
    A = [input() for _ in range(n+1)]
    S = [int(s) for s in input().split()]

    fs = S[0]   # friend's score
    w = q - S[0]    # number of question friend answered wrong
    s = 0   # your score
    for a1, a2 in zip(A[0], A[1]):
        if a1 == a2:
            if fs > 0:
                s += 1
                fs -= 1
            else:
                w -= 1
        else:
            if w > 0:
                s += 1
                w -= 1
            else:
                fs -= 1
    print('Case #{}: {}'.format(case_no, s))