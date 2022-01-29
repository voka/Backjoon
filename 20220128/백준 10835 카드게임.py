import pprint
import sys
sys.setrecursionlimit(10000000) 
N = int(input())

L_Card = list(map(int,sys.stdin.readline().split()))
R_Card = list(map(int,sys.stdin.readline().split()))

dp_check = [[-1]*(N+1) for _ in range(N+1)]


def game(l,r):
    if l == N or r == N:
        return 0
    elif dp_check[l][r] != -1:
        return dp_check[l][r]
    else:
        # 오른쪽 카드만 버릴 경우 
        if L_Card[l] > R_Card[r]:
            dp_check[l][r] = R_Card[r] + game(l,r+1)
        else:
            # 왼쪽 카드만 버릴 경우 ,# 둘 다 버릴 경우
            dp_check[l][r] = max(game(l+1,r),game(l+1,r+1))
    return dp_check[l][r]

print(game(0,0))

#pprint.pprint(dp_check)