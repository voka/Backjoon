import sys 
ip  = sys.stdin.readline 
N,K = map(int,ip().split());

class Node:
    def __init__(self,data,before = None,next=None):
        self.data = data
        self.before = before
        self.next = next

start = Node(1)
cur_node = start
for i in range(2,N+1):
    temp = Node(i,cur_node)
    cur_node.next = temp
    cur_node = temp
cur_node.next = start

answer = []
tmp = Node(0,None,start) # 시작점 만들기
while len(answer) < N:
    for i in range(K-1):
        tmp = tmp.next
    answer.append(tmp.next.data)
    tmp.next = tmp.next.next # 다음 노드 없애기 

# 출력
print("<", end = "")
for p in answer:
    print(p,end = "")
    if p != answer[-1]:
        print(", ",end='')
print(">")
    