import sys
ip = sys.stdin.readline
N,M = map(int,ip().split())
lst = list(map(int,ip().split()))
def check(t):
    tmp = M
    for l in range(M):
        tmp += t // lst[l]
    return tmp >= N
if N < M:
    print(N)
    exit()
start = 0
end = max(lst) * (N)
time = 0
while start <= end:
    mid = (start + end)//2
    if(check(mid)):
        time = mid
        end = mid - 1
    else:
        start = mid + 1
count = M
for i in range(M): # time -1 까지 놀이기구를 탄 총 인원수
    count += (time-1)//lst[i]
for i in range(M): # 마지막에 탄 놀이기구 구하기
    if time % lst[i] == 0: # t 시간에 탑승한 인원
        count += 1
    if count == N:
        print(i+1)
        break

