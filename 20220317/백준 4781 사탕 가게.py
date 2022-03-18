import sys 
ip = sys.stdin.readline
while True:
    tmp = ip().rstrip().split()
    n,m = int(tmp[0]),int(float(tmp[1])*100)
    if n == 0:
        break
    kcal, price = [], []
    for i in range(n):
        tmp = ip().rstrip().split()
        kcal.append(int(tmp[0]))
        price.append(int(float(tmp[1])*100 + 0.5))

    dp = [0]*(m+1)
    for j in range(n):
        for i in range(1,m+1):
            if i >= price[j]:
                dp[i] = max(dp[i],dp[i - price[j]] + kcal[j])
    print(dp[-1])
