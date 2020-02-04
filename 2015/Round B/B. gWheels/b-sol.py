T = int(input())
for x in range(1, T+1):
    print("Case #{}:"format(x))
    # the numbers of gears on the pedals, extra, and tire groups
    np, ne, nt = map(int, input().split())

    # the numbers of teeth on the different gears on the pedals, extra, 
    # and tire gear groups (all distinct)
    n_teeth_pedal = [int(s) for s in input().split()]
    n_teeth_extra = [int(s) for s in input().split()]
    n_teeth_tire = [int(s) for s in input().split()]

    m = int(input())    # number of questions
    p, q = [], []
    for _ in range(m):
        p_, q_ = map(int, input().split())
        p.append(p_)
        q.append(q_)

    