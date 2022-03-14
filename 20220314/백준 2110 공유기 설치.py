import sys
ip = sys.stdin.readline 
N,C = map(int,ip().split())
Xi = [int(ip()) for _ in range(N)]
Xi.sort()
#print(Xi)
len_ = len(Xi)
start = 1
end = Xi[-1] - Xi[0] # 최대 
result = 0
while start <= end:
    mid = (start+end)//2
    pre = Xi[0]
    count = 1
    for i in range(1,len_):
        if Xi[i] - pre >= mid:
            count += 1
            pre = Xi[i]
    if count >= C:
        start = mid + 1
        result = max(result,mid)
    else:
        end = mid -1
print(result)
