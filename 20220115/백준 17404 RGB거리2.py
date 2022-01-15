from sys import stdin 
N = int(stdin.readline())
dpR = [[100001 ]*3 for _ in range(N+1)] # 첫째집 R
dpG = [[100001 ]*3 for _ in range(N+1)] # 첫째집 G
dpB = [[100001 ]*3 for _ in range(N+1)] # 첫째집 B
F = list(map(int,stdin.readline().split()))
dpR[1][0] = F[0]
dpG[1][1] = F[1]
dpB[1][2] = F[2]

for j in range(2,N+1):
    R,G,B = map(int,stdin.readline().split())
    if j == N: # 마지막 색칠할 집 첫번째집과 다른곳으로 선택 
        dpR[j][2] = B + min(dpR[j-1][0], dpR[j-1][1])
        dpR[j][1] = G + min(dpR[j-1][0], dpR[j-1][2])
        dpG[j][0] = R + min(dpG[j-1][1], dpG[j-1][2])
        dpG[j][2] = B + min(dpG[j-1][0], dpG[j-1][1])
        dpB[j][0] = R + min(dpB[j-1][1], dpB[j-1][2])
        dpB[j][1] = G + min(dpB[j-1][0], dpB[j-1][2])
        break
        
    # 이번 집이 RED인 경우
    dpR[j][0] = R + min(dpR[j-1][1],dpR[j-1][2])
    dpG[j][0] = R + min(dpG[j-1][1],dpG[j-1][2])
    dpB[j][0] = R + min(dpB[j-1][1],dpB[j-1][2])
    # 이번 집이 GREEN인 경우
    dpR[j][1] = G + min(dpR[j-1][0],dpR[j-1][2])
    dpG[j][1] = G + min(dpG[j-1][0],dpG[j-1][2])
    dpB[j][1] = G + min(dpB[j-1][0],dpB[j-1][2])
    # 이번 집이 BLUE인 경우
    dpR[j][2] = B + min(dpR[j-1][0],dpR[j-1][1])
    dpG[j][2] = B + min(dpG[j-1][0],dpG[j-1][1])
    dpB[j][2] = B + min(dpB[j-1][0],dpB[j-1][1])
print(min(min(dpR[N]),min(dpG[N]),min(dpB[N])))
 
""" 
3
26 40 83
49 60 57
13 89 99

6
10 20 30
10 20 30
10 20 30
10 20 30
10 20 30
10 20 30

3
10 20 30
10 20 30
10 20 30

답:60
"""