from fractions import Fraction

T = int(input())
for x in range(1, T+1):
    _ = input() # skip empty line
    print("Case #{}:".format(x))
    np, ne, nt = map(int, input().split())

    # the numbers of teeth on the different gears on the pedals, extra, 
    # and tire gear groups (all distinct)
    pedals = [int(s) for s in input().split()]
    extras = [int(s) for s in input().split()]
    tires = [int(s) for s in input().split()]
    m = int(input())    # number of questions
    
    fraction_set = {Fraction(e1, e2) for j, e1 in enumerate(extras) \
                                     for i, e2 in enumerate(extras) if i != j}
    for _ in range(m):
        p, q = map(int, input().split())
        ans = 'No'
        for pedal in pedals:
            for tire in tires:
                if Fraction(tire, pedal) * Fraction(p, q) in fraction_set:
                    ans = 'Yes'
                    break
        print(ans)