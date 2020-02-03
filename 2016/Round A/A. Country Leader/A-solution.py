T = int(input())
for t in range(1, T+1):
    N = int(input())
    lead_name = None
    lead_unique = 0
    for _ in range(N):
        name = input()
        n_unique = len(set(name.replace(' ', '')))
        if n_unique > lead_unique or n_unique == lead_unique and name < lead_name:
            lead_name, lead_unique = name, n_unique
    print("Case #{}: {}".format(t, lead_name))