N = int(input())
NUM_List = list(map(int,input().split()))
DP = [1] * N
for i in range(N):
    for j in range(i):
            if NUM_List[j] < NUM_List[i]:
                DP[i] = max(DP[i],DP[j]+1)
print(max(DP))
    