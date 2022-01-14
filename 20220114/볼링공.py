from sys import stdin 
N, M = map(int,stdin.readline().split())
weight_list = [0]*(M+1)
weights = list(map(int,stdin.readline().split()))
for i in weights:
    weight_list[i] += 1
answer = 0
for i in range(1,M+1): # 무게 순회하면서 서로 다른 무게의 개수끼리 곱해서 더하기 
    for j in range(i+1,M+1):
        #if i == j : continue
        answer += weight_list[i]*weight_list[j]
print(weight_list)
print(answer)
""" 
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2 
"""


