from sys import stdin 


N,M = map(int,stdin.readline().split())
N_list,M_list = list(map(int,stdin.readline().split())),list(map(int,stdin.readline().split()))
"""
# 파이썬 기본정렬 사용 
NM_list = sorted(N_list+M_list)
for i in NM_list:
    print(i,end = " ")
"""
# 투포인터 방식

N_id = 0
M_id = 0
pointer_list = []
while True:
    if N_id == N and M_id == M:
        break
    if N_id == N:
        pointer_list.append(M_list[M_id])
        M_id += 1
        continue
    if M_id == M:
        pointer_list.append(N_list[N_id])
        N_id += 1
        continue
    if N_list[N_id] < M_list[M_id]:
        pointer_list.append(N_list[N_id])
        N_id += 1
    elif N_list[N_id] > M_list[M_id]:
        pointer_list.append(M_list[M_id])
        M_id += 1
    else:
        pointer_list.append(M_list[M_id])
        pointer_list.append(N_list[N_id])
        N_id += 1
        M_id += 1
for i in pointer_list:
    print(i,end = " ")