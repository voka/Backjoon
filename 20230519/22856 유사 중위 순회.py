import sys
from collections import deque
sys.setrecursionlimit(10**6)
ip = sys.stdin.readline
N = int(ip())
# 노드가 N개인 이진 트리가 있다.
# 트리를 중위 순회와 유사하게 순회하려고 한다. 이를 유사 중위 순회라고 하자.

# 순회의 시작은 트리의 루트이고 순회의 끝은 중위 순회할 때 마지막 노드이다.
# 이때 루트 노드는 항상 1번 노드이다.

# 유사 중위 순회는 루트 노드에서 시작하며, 다음과 같이 진행된다.

# 현재 위치한 노드의 왼쪽 자식 노드가 존재하고 아직 방문하지 않았다면, 왼쪽 자식 노드로 이동한다.
# 그렇지 않고 현재 위치한 노드의 오른쪽 자식 노드가 존재하고 아직 방문하지 않았다면, 오른쪽 자식 노드로 이동한다.
# 그렇지 않고 현재 노드가 유사 중위 순회의 끝이라면, 유사 중위 순회를 종료한다.
# 그렇지 않고 부모 노드가 존재한다면, 부모 노드로 이동한다.
# 유사 중위 순회를 종료할 때까지 1 ~ 4를 반복한다.
# 여기서 이동이라는 것은 하나의 노드에서 다른 노드로 한번 움직이는 것을 의미한다.
# 예를 들면, 노드 1에서 노드 2로 가는 것을 한번 이동하였다고 한다.

# 유사 중위 순회를 하면서 이동한 횟수를 구하려고 한다.

# 첫 번째 줄에 트리를 구성하는 노드의 개수 N이 주어진다.

# 두 번째 줄부터
# $N + 1$ 번째 줄까지 현재 노드
# $a$, 현재 노드의 왼쪽 자식 노드
# $b$, 현재 노드의 오른쪽 자식 노드
# $c$가 공백으로 구분되어 주어진다. 만약 자식 노드의 번호가 -1인 경우 자식 노드가 없다는 것을 의미한다.
nodes = [[-1, -1, -1] for _ in range(N+1)]  # 부모 인덱스, 왼쪽, 오른쪽 자식 인덱스

for _ in range(N):
    p, a, b = map(int, ip().split())
    if a != -1:
        nodes[p][1] = a  # 자식 노드 설정
        nodes[a][0] = p  # 부모 노드 설정
    if b != -1:
        nodes[p][2] = b
        nodes[b][0] = p

total_count = 0
right_count = 0


def find_end(idx):
    global right_count, last_idx
    right_count += 1
    if nodes[idx][2] == -1:
        last_idx = idx
        return
    find_end(nodes[idx][2])


last_idx = find_end(1)

# print(right_count)


def gogogo(idx):
    global total_count, flag
    if nodes[idx][1] != -1:
        gogogo(nodes[idx][1])
        total_count += 1
    total_count += 1
    if nodes[idx][2] != -1:
        gogogo(nodes[idx][2])
        total_count += 1


if N == 1:
    print(0)
else:
    gogogo(1)
    print(total_count - right_count)
