import sys
sys.setrecursionlimit(1000000)
N,M = map(int,input().split())
lens = []
for i in range(N):
    lens.append(int(sys.stdin.readline().strip()))
lens.sort()
lenslen = len(lens)
def Lower_Bound(left,right,target):
    while left < right:
        Mid = left + (right-left) //2
        if lens[Mid] < target:
            left = Mid + 1
        else:
            right = Mid
    return right

def check(H):
    taken = 0
    S_index = Lower_Bound(0,lenslen-1,H)
    #print(S_index)
    for i in range(S_index,lenslen):
        taken += lens[i]//H
    #print(M)
    if taken >= M:
        return True
    else:
        return False
    
def Solve():
    answer = 0
    left = 0
    right = pow(2,31)
    while left <= right:
        mid = (left+right) // 2
        if check(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid -1 
    return answer
    

print(Solve())
