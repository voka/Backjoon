from collections import deque
N,K = map(int,input().split())
check = [[-1]*500001 for _ in range(2)] # 홀짝 구분
myq = deque()
check[0][N] = 0
myq.append((N,K,0))
while myq:
    cur,cur_K,t = myq.popleft()
    if cur_K > 500000:
        print(-1)
        break
    f = t%2
    if check[f][cur_K] != -1:
        print(t)
        break
    nt = 1-f
    #print(nt,t)
    for nk in (cur-1,cur+1,cur*2):
        if -1 < nk < 500001 and check[nt][nk] == -1:
            check[nt][nk]  = 1
            myq.append((nk,cur_K+t+1,t+1))
'''
17 -> 16 -> 15 -> 16 -> 15
5 -> 6 -> 8 -> 11 -> 15

1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 31
10 -> 11 -> 13 -> 16 -> 20 -> 25 -> 31

'''