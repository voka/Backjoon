import sys
ip = sys.stdin.readline
for _ in range(3):
    N = int(ip())
    coins = [list(map(int, ip().split())) for _ in range(N)]
    m = sum(money * cnt for [money, cnt] in coins)
    dp = [0]*(m//2+1)
    if m % 2 != 0:
        print(0)
    else:
        for [money, cnt] in coins:
            for i in range(1, cnt+1):
                if money * i <= m//2:
                    dp[money*i] = 1
                for j in range(m//2, money*i, -1):
                    if dp[j] == 1:
                        continue
                    if (dp[j - money*i] != 0):
                        dp[j] = 1
        print(dp[m//2])
