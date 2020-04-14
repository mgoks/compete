# inefficient but short
for case_no in range(1, int(input()) + 1):
    raw_str = ''.join([int(x) * '(' + x + ')' * int(x) for x in input()])
    for _ in range(9):
        raw_str = raw_str.replace(')(', '')
    print("Case #{}: {}".format(case_no, raw_str))

"""
keep track of open parantheses n
for each digit d open or close parantheses until n = d
"""
# for t in range(1, int(input()) + 1):
#     cur = 0
#     S = [int(char) for char in input()]
#     y = []
#     for target in S:
#         if cur < target:
#             while cur < target:
#                 y.append('(')
#                 cur += 1
#         elif cur > target:
#             while cur > target:
#                 y.append(')')
#                 cur -= 1
#         y.append(str(target))
#     y.append(')' * cur)
#     print('Case #{}: {}'.format(t, ''.join(y)))
    