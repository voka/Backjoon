import sys
ip = sys.stdin.readline
D, K = map(int, ip().split())
fibo = [1]*D
while True:
    for i in range(2, D):
        fibo[i] = fibo[i-1] + fibo[i-2]
    if fibo[D-1] == K:
        print(fibo[0])
        print(fibo[1])
        break
    elif fibo[-1] > K:
        fibo[0] += 1
        fibo[1] = fibo[0]
    else:
        fibo[1] += 1
