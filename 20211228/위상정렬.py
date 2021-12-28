from queue import Queue

def TopologySort(Nodes, indegree):
    result = []
    queue = Queue()
    for i in range(1,len(Nodes)):
        if(indegree[i] == 0) : 
            queue.put(i)
    for i in range(1,len(Nodes)):
        if queue.empty() : break
        cur_node = queue.get()
        result.append(cur_node)
        for j in range(len(Nodes[cur_node])):
            next_node = Nodes[cur_node][j]
            indegree[next_node] -= 1
            if(indegree[next_node] == 0): queue.put(next_node)
    
    for i in result:
        print(i,end=' ')

def main():
    N,M = map(int,input().split())
    indegree = [0]*(N+1)
    Nodes = [[] for _ in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        Nodes[a].append(b)
        indegree[b] += 1
    TopologySort(Nodes, indegree)
main()