import sys
ip = sys.stdin.readline
N = int(ip())
lines = ip().strip()

cur_L = 0
answer = 1
for i in lines:
    if i == 'S':
        answer += 1
    elif i == 'L':
        cur_L += 1
        if cur_L == 2:
            cur_L = 0
            answer += 1
if answer > N :
    print(N)
else:
    print(answer)