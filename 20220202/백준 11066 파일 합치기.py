

# 1 2 3 4 5
""" 
1 + 2 = 3 (3)
3 + 3 = 6 (3 + 6)
6 + 4 = 10 (3 + 6 + 10)
10 + 5 = 15 (3 + 6 + 10 + 15)
34

1 + 2 = 3 (3)
3 + 4 = 7 (3 + 7)
3 + 5 = 8 (3 + 7 + 8)
7 + 8 = 15 (3 + 7 + 8 + 15)
33
"""
import sys,math
def main():
    K = int(input())
    files = list(map(int,sys.stdin.readline().split()))
    dp = [[0]*K for _ in range(K)] # i 번째 부터 j번째 까지의 파일을 합친 최소비용 
    for x in range(1,K):
        for i in range(K-x):
            j = i+x
            dp[i][j] = math.inf
            tmp = sum(files[i:j+1])
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+tmp)
    print(dp[0][K-1])

T = int(input())
for _ in range(T): main()