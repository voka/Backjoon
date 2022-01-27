import sys
inp = sys.stdin.readline().strip()
N = int(inp)
cnt = [1000001]*1000001
cnt[0] = -1
cnt[1] = 0
cnt[2] = 1
cnt[3] = 1
cnt[4] = 2
for i in range(5,N+1):
    if i % 2 == 0 :
        cnt[i] = min(cnt[i],cnt[i//2]+1)
    if i % 3 == 0 :
        cnt[i] = min(cnt[i],cnt[i//3]+1)
    cnt[i] = min(cnt[i],cnt[i-1]+1)
print(cnt[N])
cur = N
for i in range(cnt[N]):
    print(cur,end = " ")
    if cnt[cur//3] + 1 == cnt[cur] and cur % 3 == 0:
        cur = cur//3
    elif cnt[cur//2] + 1 == cnt[cur] and cur % 2 == 0:
        cur = cur//2
    elif cnt[cur-1] + 1 == cnt[cur]:
        cur = cur - 1
print(1)
        