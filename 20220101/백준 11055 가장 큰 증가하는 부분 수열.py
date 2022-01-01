from sys import stdin
N = int(stdin.readline())
boxs = list(map(int,stdin.readline().split()))
DP = [0] * N
for i in range(N):
    DP[i] = boxs[i] # 
    for j in range(i):
            if boxs[j] < boxs[i]:# 증가수열 중에
                DP[i] = max(DP[i],DP[j]+boxs[i]) # 값이 큰놈
print(max(DP))
# 증가하는 부분 순열의 최대값을 찾으면 되는 문제 