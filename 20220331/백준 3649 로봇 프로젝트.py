import sys
ip = sys.stdin.readline 
while True:
    try:
        x = int(ip())
        X = x*10000000
        N = int(ip())
        lego = [int(ip()) for _ in range(N)]
        lego.sort()
        answer = ((0,0))
        start,end = 0,N-1
        while start < end:
            target = lego[start] + lego[end]
            if target == X:
                answer = ((lego[start],lego[end]))
                break
            elif target < X:
                start += 1
            else:
                end -= 1
        if answer != (0,0):
            print("yes {0} {1}".format(answer[0],answer[1]))
        else:
            print("danger")
    except:
        break
    