import sys
N = int(input())
data = {}
l = list(map(int,sys.stdin.readline().split()))
for i in l:
    data[i] = 1
answer = sorted(data.keys())
print(*answer)
 