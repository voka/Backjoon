import sys
sys.setrecursionlimit(10000000)
N = int(input())
NList = list(map(int,sys.stdin.readline().split()))
M = int(input())
MList = list(map(int,sys.stdin.readline().split()))
NList.sort() # 무조건 정렬된 상태에서 진행 

def binary_search(Start,End,Target):  # 이진탐색 알고리즘
    if Start > End:
        return None
    Mid = (Start + End) // 2
    if NList[Mid] == Target:
        return Mid
    elif NList[Mid] > Target:
        return binary_search(Start,Mid-1,Target)
    else:
        return binary_search(Mid+1,End,Target)
for m in MList:
    if binary_search(0,N-1,m) != None:
        print(1)
    else:
        print(0)