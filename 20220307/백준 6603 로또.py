import sys
from itertools import combinations
ip = sys.stdin.readline
while True:
    lst = ip().strip()
    if lst == '0':
        break
        exit()
    nums = list(map(int,lst.split()))
    K = nums[0]
    new_lst = nums[1:]
    lotto_nums = combinations(new_lst, 6)
    for l in lotto_nums:
        print(*l)
    print()