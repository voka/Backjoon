import sys
ip = sys.stdin.readline

T = int(ip())
for i in range(T):
    N = int(ip())
    mydict = {}
    num_list = list(map(int,ip().split()))
    for j in range(N):
        mydict[num_list[j]] = 1
    Q = int(ip())
    num_list = list(map(int,ip().split()))
    for j in range(Q):
        if num_list[j] in mydict:
            print(1)
        else:
            print(0)
        