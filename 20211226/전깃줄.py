# 왼쪽 전봇대 기준으로 Line을 정렬한다.
# 왼쪽 전봇대 값이 정렬된 상태에서 오른쪽 값이 증가하는 수열이면 전깃줄이 겹치지 않는다.  
# 그래서 오른쪽 전봇대의 Line에서 가장 긴 증가하는 부분 수열을 찾는다. 
# 전체 개수 N에서 가장 긴 증가하는 부분 수열을 빼면 제거해야하는 전기줄 수를 구할 수 있다.

N = int(input())
lines = [list(map(int,input().split())) for _ in range(N)]
lines.sort()
DP = [1] * N
NUM_List = [lines[i][1] for i in range(N)] 
for i in range(N):
    for j in range(i):
            if NUM_List[j] < NUM_List[i]:
                DP[i] = max(DP[i],DP[j]+1)
print(N-max(DP))