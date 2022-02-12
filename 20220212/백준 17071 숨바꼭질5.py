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
    """ 
    f -> 홀수인지 짝수인지 구분하는 flag
    if check[f][cur_K] != -1: <- 요놈의 의미는
    1. 현재 시간이 홀수일때 cur_K인 지점을 홀수 시간대에 방문했다.
    2. 현재 시간이 짝수일때 cur_K인 지점을 짝수 시간대에 방문했다. 
    위 두 가지 경우 그 지점을 앞뒤(cur+1 -> cur-1)로 이동하면서 해당 지점을 지켰다고 가정하고 
    K가 이동해서 cur_K가 된 시점의 시간인 t를 출력하겠다는 뜻이다. 
    
    cur == cur_K인 경우도 아래의 경우에 포함되는데,
    cur == cur_K라면
    현재 시간인 t 시점에 check[f][cur] = check[f][cur_K] = 1 이고 
    check[f][cur_K] != -1이라 t를 출력하게 된다. 
    """
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