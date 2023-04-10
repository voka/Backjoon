import sys
from collections import deque
ip = sys.stdin.readline
N, M, K = map(int, ip().split())
# M -> 건물 사이 관계의 수
# K -> 게임 정보
# N -> 건물 종류의 개수

graph = [[] for _ in range(N+1)]
check = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, ip().split())
    graph[b].append(a)
    check[a].append(b)

instruct = {}

answer = "King-God-Emperor"

can_instruct = [0]*(N+1)


def add(a):
    if can_instruct[a] == 0:
        for must in graph[a]:
            if must not in instruct or instruct[must] == 0:
                return False
    can_instruct[a] = 1
    if a in instruct:
        instruct[a] += 1
    else:
        instruct[a] = 1
    return True


def destroy(a):
    if a not in instruct or instruct[a] == 0:
        return False
    instruct[a] -= 1
    if instruct[a] == 0:
        for c in check[a]:
            can_instruct[c] = 0
    return True


for i in range(K):
    do, a = map(int, ip().split())
    if do == 1:
        if add(a) == False:
            answer = "Lier!"
            break
    elif do == 2:
        if destroy(a) == False:
            answer = "Lier!"
            break
print(answer)
