import sys
ip = sys.stdin.readline
N = int(ip())
plans =  [tuple(map(int,ip().split())) for _ in range(N)]
plans.sort(key = lambda x : (-x[1],x[0]))
answer = [0]*(1001)
for i in range(N):
    d,w = plans[i]
    for j in range(d,0,-1):
        if answer[j] < w:
            answer[j] = w
            break
#print(plans)
print(sum(answer))
#print(answer)
