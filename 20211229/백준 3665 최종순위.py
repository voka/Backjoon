from queue import Queue
from sys import stdin
def main():
    N = int(stdin.readline())
    indegree = [0] * (N+1)
    last_year = list(map(int,stdin.readline().split()))
    Nodes = [[0 for i in range(N+1)] for _ in range(N+1)]
    for b in range(len(last_year)): # a -> b 순서 
        for a in range(b+1,len(last_year)):
            Nodes[last_year[b]][last_year[a]] = 1
    M = int(stdin.readline())
    for i in range(M):# 등수가 뒤바뀜!!!! a 가 b보다 앞선다는게 아님 ㅇㅇ 
        a,b = map(int,stdin.readline().split())
        Nodes[a][b], Nodes[b][a] = Nodes[b][a], Nodes[a][b] 
    que = Queue()    
    start_c = 0
    for i in range(1,N+1):
        indegree[i] = N - 1 - Nodes[i].count(1)
        if indegree[i] == 0:
            que.put(i)
            start_c+=1
        if(start_c > 1):
            print("?")
            return 
    #print(Nodes,indegree)
    result = []
    #miniresult = [i for i in range(1,N+1)] 
    #진입차수 만으로 정렬한 것도 정답이랑 일치하지만 사이클을 어떻게 찾아낼지를 모르겠음.
    #k = sorted(miniresult, key=lambda x : indegree[x]) 
    #print(k)
    while not que.empty():
        cur = que.get()
        result.append(cur)
        for i in range(len(Nodes[cur])):
            if Nodes[cur][i] == 0 : continue
            indegree[i] -= 1
            if indegree[i] == 0:
                que.put(i)
    #print(result)
    if len(result) != N:
        print("IMPOSSIBLE")
    else:
        for j in result:
            print(j,end = " ")
        print()

T = int(stdin.readline())
for i in range(T) : main()