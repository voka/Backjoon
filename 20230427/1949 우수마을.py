import sys
sys.setrecursionlimit(10**9)
ip = sys.stdin.readline
N = int(ip())
populations = [0] + list(map(int, ip().split()))
graph = [[] for _ in range(N+1)]
# dp[i][0] -> i번째 마을이 우수마을이 아닐 경우 최대값, dp[i][1] -> i번째 마을이 우수마을 일 경우 최댓값
dp = [[0]*2 for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, ip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
visited[1] = 0


def dfs(idx):
    visited[idx] = 1
    dp[idx][1] = populations[idx]  # 우수마을이면 인구수 더하기
    dp[idx][0] = 0
    for i in graph[idx]:
        if visited[i] == 1:
            continue
        dfs(i)
        dp[idx][1] += dp[i][0]  # idx 마을이 우수마을이면 다음 마을은 일반 마을이어야 함
        # idx 마을이 우수마을이 아니면 다음 마을이 우수마을이던 이니던 상관없음
        dp[idx][0] += max(dp[i])


dfs(1)  # 1번 마을에서 시작
print(max(dp[1]))  # 1번마을이 우수마을인 경우, 아닌경우 중 최대 인구수를 가진 경우 출력
