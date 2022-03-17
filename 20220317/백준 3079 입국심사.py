import sys
ip = sys.stdin.readline 
N,M = map(int,ip().split())
Times = []
for i in range(N):
    Times.append(int(ip()))
start = 1
end = max(Times)*(M)
answer = 0
def check(t):
    temp = 0
    for j in range(N):
        temp += t//Times[j]
    return temp >= M
while start <= end:
    mid = (start + end)//2 
    if check(mid):
        end = mid -1
        answer = mid
    else:
        start = mid + 1
print(answer)
