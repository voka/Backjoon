from sys import stdin 
n = int(stdin.readline())
c = n
if n < 5:
    c = 5
dp = [n]*(c+1)
dp[2] = 1
dp[5] = 1
cur1 = 2
cur2 = 5
if n%5 == 0:
    print(int(n/5))
else:
    i=2
    while True:
        if n-i == -1 or n-i == 1 or n-i == 3:
            print(-1)
            break
        if (n-i)%5 == 0:
            print(int(i/2 + (n-i)/5))
            break
        i += 2
        
""" 
dp[7] = 1 + 1
dp[9] = 1 + 1 + 1
dp[10] = 1 + 1
1
2 : 1
3 : 
4 : 2
5 : 1
6 : 3
7 : 2
8 : 4
9 : 3
10 : 2
11 : 4
12 : 3
13 : 5
14 : 4
15 : 3 -> dp[10] + dp[5]
16 : 5 -> dp[10] + 3 = dp[6]
17 : 4 -> dp[15] + 1 = dp[2]
18 : 6 -> dp[10] + 4 = dp[8]
19 : 5 -> dp[15] + 2 = dp[4]
20 : 4 -> dp[15] + 1 = dp[15] + dp[5]
21 : 6 -> dp[15] + 3

"""