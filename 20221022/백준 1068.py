import sys
from collections import deque
ip = sys.stdin.readline

N = int(input())
Mylist = list(map(int, input().split()))
Delete_node = int(input())
answer = 0

def DFS(mylist, node):
    que = deque()
    que.append(node)
    visited = []
    while que:
        cur = que.pop()
        visited.append(cur)
        mylist[cur] = -10
        for i in range(len(mylist)):
            if i not in visited and cur == mylist[i]:
                que.append(i)


DFS(Mylist,Delete_node)
answer = 0
for i in range(len(Mylist)):
    if Mylist[i] != -10 and i not in Mylist:
        answer += 1
print(answer)