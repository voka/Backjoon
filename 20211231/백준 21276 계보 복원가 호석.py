from queue import Queue
from sys import stdin 

que = Queue()
N = int(stdin.readline())
name = {} # 이름 -> 숫자 사전 --> 위상정렬시 사용
answer_name = {} # 숫자 -> 이름 사전 --> 정답출력시 사용
names = stdin.readline().replace('\n','').split()
for i in range(N):
    name[names[i]] = i+1
    answer_name[i+1] = names[i]
M = int(stdin.readline())
Nodes = [[] for _ in range(N+1)]
indegree = [0] *(N+1)
for i in range(M): # 여기에 M 대신에 N 적었다가... Value_error 발생함... 젠장..
    a,b = stdin.readline().replace('\n','').split()
    # 위상정렬시 편리하게 노드와 진입차수는 이름을 숫자로 변환해서 입력
    Nodes[name[b]].append(name[a]) 
    indegree[name[a]] += 1
rank1 = [] # 시조들의 이름
for j in range(1,N+1):
    if(indegree[j] == 0):
        rank1.append(answer_name[j])
        que.put(j)
result = [[] for _ in range(N+1)]
while not que.empty():
    cur = que.get()
    for j in Nodes[cur]:
        indegree[j] -= 1
        if(indegree[j] == 0):
            que.put(j)
            # 진입차수가 0 일 경우에만 직접 자손이 된다. , 그렇지 않을경우 자식들의 자식까지도 결과에 포함되어 버린다.
            result[cur].append(answer_name[j]) 
print(len(rank1))
rank1.sort() # 조상 이름 정렬
print(" ".join (rank1)) # 조상 이름 출력
answers = []
for i in range(1,len(result)):
    temp = "{0} {1}".format(answer_name[i], len(result[i]))
    result[i].sort() # 자식 이름 정렬
    temp += " {}".format(" ".join(result[i]))
    answers.append(temp) # "자신이름" "자식수" "자식이름들" 형태 
answers.sort() # 자신의 이름으로 정렬 
for i in answers:
    print(i)