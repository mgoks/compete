T = int(input())
for x in range(1, T+1):
    _ = input() # skip empty line
    print("Case #{}:".format(x))
    # the numbers of gears on the pedals, extra, and tire groups
    np, ne, nt = map(int, input().split())

    # the numbers of teeth on the different gears on the pedals, extra, 
    # and tire gear groups (all distinct)
    n_teeth_pedal = [int(s) for s in input().split()]
    n_teeth_extra = [int(s) for s in input().split()]
    n_teeth_tire = [int(s) for s in input().split()]

    m = int(input())    # number of questions
    for _ in range(m):
        # p/q = pedals/extra1 * extra2/tire
        p, q = map(int, input().split())
        possible = 'No'
        for pedal in n_teeth_pedal:
            for extra1 in n_teeth_extra:
                for extra2 in n_teeth_extra:
                    if extra1 != extra2:
                        for tire in n_teeth_tire:
                            if p/q == pedal/extra1 * extra2/tire:
                                print('pedal', pedal, 'extra1', extra1, 'extra2', extra2, 'tire', tire)
                                possible = 'Yes'
        print(possible)
    # print('')