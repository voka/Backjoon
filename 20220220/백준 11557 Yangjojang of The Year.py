import sys
ip = sys.stdin.readline
T = int(ip())
for _ in range(T):
    N = int(ip())
    tmp = []
    for i in range(N):
        name,num = ip().split()
        num = int(num)
        tmp.append((num,name))
    answers = sorted(tmp,key=lambda x:-x[0])
    print(answers[0][1])
