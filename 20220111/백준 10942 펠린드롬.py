from sys import stdin 
N = int(stdin.readline())
numbers = list(map(int,stdin.readline().split()))
dp = [[0]*(N) for _ in range(N)]
for l in range(N):
    for s in range(N-l):
        e = s + l        
        if s == e :
            dp[s][e] = 1
        elif numbers[s] == numbers[e]: # 양 끝쪽 글자가 같을 경우 
            if dp[s+1][e-1] == 1 or s + 1 == e: # s+1 ~ e-1이 펠린드롬이거나 길이가 2인 경우 
                dp[s][e] = 1

M = int(stdin.readline())

for i in range(M):
    a,b = map(int,stdin.readline().split())
    print(dp[a-1][b-1])
# 펠린드롬인 경우
# 숫자가 모두 동일한 경우 min == max
"""  --> 시간초과
while not myque.empty():
    S,E = myque.get()
    if S-1 > 0 and dp[S-1][E] != 1:
        if max(numbers[S-1:E+1]) == min(numbers[S-1:E+1]):
            dp[S-1][E] = 1
            myque.put((S-1,E))
    if E+1 <= N and  dp[S][E+1] != 1:
        if max(numbers[S:E+2]) == min(numbers[S:E+2]):
            dp[S][E+1] = 1
            myque.put((S,E+1))
    if S-1 > 0 and E+1 <= N and numbers[S-1] == numbers[E+1]:
        dp[S-1][E+1] = 1
        myque.put((S-1,E+1))
        
--> 펠린드롬 확인하는 부분 
for k in range(N):
    for j in range(k,N):
        if dp[k][j] == 1:
            print(numbers[k:j+1])

7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7

"""