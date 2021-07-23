T = int(input())
while(T):
    T -= 1
    k = int(input())
    n = int(input())
    dp = [[ i for i in range(n)] for j in range(k + 1) ]
    print(dp)