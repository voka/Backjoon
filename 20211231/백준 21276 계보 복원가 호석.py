from queue import Queue
from sys import stdin 

que = Queue()
N = int(stdin.readline())
name = {}
answer_name = {}
for i in range(N):
    n = stdin.readline().replace('\n','')
    name[i] = n
    answer_name[n] = i
Words = [[] for _ in range(11)]
indegree = [0] *(11)
dict = {}
result_dict = {}
for i in range(N):
    letters = stdin.readline().replace('\n','')
    for k in letters:
        if k not in dict:
            result_dict[len(dict) + 1] = k
            dict[k] = len(dict) + 1
    for j in range(2,len(letters)):
        Words[dict[letters[j-1]]].append(dict[letters[j]])
        indegree[dict[letters[j]]] += 1
cur_N = len(dict)
cnt = 0
for j in range(1,cur_N+1):
    if(indegree[j] == 0):
        cnt += 1
        que.put(j)
    if(cnt > 2):
        print("?")
        exit()
result = []
while not que.empty():
    cur = que.get()
    result.append(cur)
    for j in Words[cur]:
        indegree[j] -= 1
        if(indegree[j] == 0):
            que.put(j)
print(result)
for i in result:
    print(result_dict[i],end=" ")
if(len(result) != cur_N):
    print("!")
else:
    for i in result:
        print(result_dict[i],end=" ")
    
print (Words,indegree)
        
print(dict)