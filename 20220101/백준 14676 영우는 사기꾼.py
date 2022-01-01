from queue import Queue
from sys import stdin

que = Queue()
N,M,K = map(int,stdin.readline().split()) # 총 노드 수, 주어지는 관계 수, 게임 내용(건물 짓기 or 파괴하기) 수
Nodes = [[] for _ in range(N+1)]
Back_Nodes = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for i in range(M): # 입력받기
    a,b = map(int,stdin.readline().split())
    Nodes[a].append(b)
    Back_Nodes[b].append(a)
    indegree[b] += 1
    
for i in range(1,N+1): # 진입차수 0인거 que에 삽입
    if(indegree[i] == 0):
        que.put(i)
        
indegree_copy = indegree[:] # 진입차수 복사본
result = []

while not que.empty(): # 위상정렬
    cur = que.get()
    result.append(cur)
    for i in Nodes[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.put(i)     

check = [0]*(N+1) # 건물을 파괴할 수 있는지 확인
num = [0]*(N+1) # 지어진 건물의 개수를 확인
check[result[0]] = 1
for i in Nodes[result[0]]:
    indegree_copy[i] -= 1
answer = 1 

# 처음에는 가장 쉬워 보이는 Back_Nodes를 만들어 해당 건물을 건설할때 
# 선행조건들을 모두 만족시키면 짓도록 코드를 구성했습니다.
# 그러다보니 시간초과가 발생했습니다.
# 그래서 위상정렬의 아이디어를 빌려 진입차수의 복사복을 만들어 이용했습니다.

# 건물을 짓는 경우
# 건물을 지을 때 진입차수를 확인해서 진입차수가 0이면 지어지도록 했습니다. 
# 그래서 추가적으로 해당 건물의 Nodes에 들어있는 건물들의 진입차수를 -1해줍니다.
# 그리고 num배열을 새롭게 만들어 만들어진 건물의 개수를 저장하도록 했습니다.

# 건물을 파괴하는 경우
# 건물의 개수가 담긴 배열에서 현재 건물의 개수를 확인합니다. 
# 건물을 파괴하고 나서 해당 건물의 개수가 0개이면 연관된 건물들의 진입차수를 +1 해줍니다.
# 지어진 건물의 개수가 1보다 작으면 answer을 0으로 만들고 입력값만 계속 받습니다.
for i in range(K):
    a,b = map(int,stdin.readline().split())
    if answer == 0:
        continue
    if a == 1: # 건물을 짓는 경우
        if indegree_copy[b] == 0:
            for j in Nodes[b]:
                if(indegree_copy[j]>0) : indegree_copy[j] -= 1
            num[b] += 1
        else:
            answer = 0
    elif a == 2:# 건물을 파괴하는 경우
        if num[b] > 0:
            num[b] -= 1
            if num[b] == 0:
                for j in Nodes[b]:
                    indegree_copy[j] += 1
        else:
            answer = 0

if answer :
    print ("King-God-Emperor")
else:
    print("Lier!")
    
