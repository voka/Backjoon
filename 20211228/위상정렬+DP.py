from collections import deque
from queue import Queue
from sys import stdin
# Dp 작업과 위상정렬을 따로 해야 한다고 생각해 두번 시간초과남.
# 위상정렬 하면서 DP하는 것을 생각을 못함....
# 아 그게 문제가 아니라 입력받는걸 input으로 해서 시간초과남.... 
"""
dp[1] = times[1]
1 -> 2,3
dp[2] = min(dp[1] + times[2],dp[2])
dp[3] = dp[1] + times[3]
2-> 4,5
dp[4] = dp[2] + times[4]
dp[5] = dp[2] + times[5]
3->6
dp[6] = dp[2] + times[6]

5->7
dp[7] = dp[5] + times[7]

    
"""
    
def main():
    N,M = map(int,stdin.readline().split())
    indegree = [0]*(N+1)
    Nodes = [[] for _ in range(N+1)]
    times = list(map(int,stdin.readline().split())) # 건물 짓는 시간
    for i in range(M):
        a,b = map(int,stdin.readline().split())
        Nodes[a].append(b)
        indegree[b] += 1
    win_condition = int(stdin.readline()) # 해당 번호의 건물을 지을 경우 승리
    
    # Topological_Sort_with_DP
    result = []
    dp = [0] * (N+1) # dp[N] =:> 건물 번호 N을 짓는데 걸리는 최소시간
    queue = Queue() # 건물번호
    for i in range(1,N+1):
        if(indegree[i] == 0) : 
            dp[i] = times[i-1] # 첫번째로 지을 수 있는 건물들
            queue.put(i)
    while queue:
        cur_node = queue.get()
        if cur_node == win_condition : break
        result.append(cur_node)
        for j in Nodes[cur_node]:
            dp[j] = max(dp[cur_node]+times[j-1],dp[j])
            indegree[j] -= 1
            if(indegree[j] == 0): 
                queue.put(j)
    print(dp[win_condition])
    
T = int(stdin.readline())
for i in range(T) : main()

