import sys
sys.setrecursionlimit(1000000)
N,M = map(int,input().split())
namos = list(map(int,sys.stdin.readline().split()))
namos.sort()
namolen = len(namos)
def Lower_Bound(left,right,target):
    while left < right:
        Mid = left + (right-left) //2
        if namos[Mid] < target:
            left = Mid + 1
        else:
            right = Mid
    return right

def check(H):
    taken = 0
    S_index = Lower_Bound(0,namolen-1,H)
    #print(S_index)
    for i in range(S_index,namolen):
        if namos[i] >= H:
            taken += (namos[i] - H)
    #print(M)
    if taken >= M:
        return True
    else:
        return False
    
def Solve():
    answer = 0
    left = 0
    right = 1000000001
    while left <= right:
        mid = (left+right) // 2
        if check(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid -1 
    return answer
    

if M == 0:
    print(namos[-1])
else:    
    print(Solve())
