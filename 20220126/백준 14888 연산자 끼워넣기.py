import sys 
N = int(input())
nums = list(map(int,sys.stdin.readline().split()))
dumps = list(map(int,sys.stdin.readline().split()))
answer = [1000000000,-1000000000]
def DFS(n,result):
    if n == N:
        answer[1] = max(answer[1],result)
        answer[0] = min(answer[0],result)
        return
    for i in range(4):
        if dumps[i] > 0:
            #print(n,calcaulate(result,nums[n],i))
            dumps[i] -= 1
            if i == 0:
                DFS(n+1,result+nums[n])
            elif i == 1:
                DFS(n+1,result-nums[n])
            elif i == 2:
                DFS(n+1,result*nums[n])
            else:
                DFS(n+1,int(result/nums[n]))
            dumps[i] += 1
    return 
DFS(1,nums[0])
print(answer[1])
print(answer[0])