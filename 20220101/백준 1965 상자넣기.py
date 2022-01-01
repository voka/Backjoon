from sys import stdin
N = int(stdin.readline())
boxs = list(map(int,stdin.readline().split()))
DP = [1] * N
for i in range(N):
    for j in range(i):
            if boxs[j] < boxs[i]:
                DP[i] = max(DP[i],DP[j]+1)
print(max(DP))
# 증가하는 부분 순열의 최대값을 찾으면 되는 문제 