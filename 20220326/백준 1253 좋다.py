import sys
ip = sys.stdin.readline 
N = int(ip())
lst = list(map(int,ip().split()))
lst.sort()

answer = 0
for i in range(N):
    temparray = lst[:i] + lst[i+1:]
    start,end = 0,N-2
    while start < end:
        tmp = temparray[start] + temparray[end]
        if tmp == lst[i]:
            answer += 1
            break
        if tmp < lst[i] :
            start += 1
        else:
            end -= 1
print(answer) 