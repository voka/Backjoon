""" 
2 + 1 1,3
5 + 1 1,6
5 + 3 3,6
--------
3 + 6 + 8
-> 17


3 + 2 2,4
4 + 4 4,5
4 + 2 2,5
--------
5 + 8 + 6 => 19

"""
import sys,pprint
from itertools import combinations
N = int(sys.stdin.readline())
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#print(maps)
idxs = [i for i in range(1,N+1)]
nums = list(combinations(idxs, N//2))
#pprint.pprint(nums)
def calculate(a,b):
    a_sum = 0
    b_sum = 0
    for i in range(N//2):
        for j in range(i+1,N//2):
            #print(a[i],a[j],b[i],b[j])
            a_sum += maps[a[i]-1][a[j]-1]
            a_sum += maps[a[j]-1][a[i]-1]
            b_sum += maps[b[i]-1][b[j]-1]
            b_sum += maps[b[j]-1][b[i]-1]
    return(abs(a_sum-b_sum))
answer = N*10000000
for i in range(len(nums)//2):
    answer = min(answer,calculate(nums[i],nums[-i-1]))
print(answer)