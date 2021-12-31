from queue import Queue
from sys import stdin
que = Queue()

def main():
    K,M,P = map(int,stdin.readline().split())
    Nodes = [[] for _ in range(M+1)]
    indegree = [0]*(M+1)
    strahler_Order = [[0,0] for _ in range(M+1)]
    for i in range(P):
        a,b = map(int,stdin.readline().split())
        Nodes[a].append(b)
        indegree[b] += 1 
    for i in range(1,M+1):
        if(indegree[i] == 0):
            strahler_Order[i] = [1,1]
            que.put(i)
    # 진입차수 == 0 -> 앞의 선행조건을 모두 만족했다는 소리
    while not que.empty():
        cur = que.get()
        for i in Nodes[cur]:
            cur_max = max(strahler_Order[cur])
            i_max = max(strahler_Order[i])
            #print(cur_max,end = " ")
            if cur_max > i_max : # 순서 값이 큰 경우 바로 바꿔준다.
                strahler_Order[i] = [cur_max,1]
            elif cur_max == i_max : # 순서 값이 같은게 들어온 경우 개수를 늘려준다.
                strahler_Order[i][1] += 1
            indegree[i] -= 1
            if(indegree[i] == 0):
                que.put(i)
                # 큐에 삽입된다 --> 들어오는 모든 강을 다 탐색했다. 
                if strahler_Order[i][1] >= 2:
                    strahler_Order[i] = [strahler_Order[i][0]+1,1]
    #print(strahler_Order,indegree)
    
    #print(result)
    # 정답 출력
    print("{0} {1}".format(K,strahler_Order[M][0]))    

T = int(stdin.readline())
for i in range(T): main()