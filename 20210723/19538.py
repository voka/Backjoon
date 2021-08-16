class Graph():
    def __init__(self,N):
        self.maps = [[] for j in range(N+1)]
        self.rumor = [0 for j in range(N+1)]
        self.check = [0 for j in range(N+1)]
        self.counts = [N+10 for j in range(N+1)]
        self.queue = []
        self.N = N
    
    def set(self,infos,id):
        for i in infos:
            if(i == 0) : break
            self.maps[id].append(i)
        #print(id,self.maps[id],len(self.maps[id])) 
    
    def BFS(self,x):
        for i in x:   
            self.queue.append((i,0))
            self.counts[i] = 0
        while(len(self.queue) != 0):
            next,cur_c = self.queue.pop(0)
            self.counts[next] = min(cur_c,self.counts[next])
            self.check[next] = 1
            for j in self.maps[next]:
                self.rumor[j] += 1
            next_c = cur_c + 1
            for j in self.maps[next]:
                if(self.check[j] == 1) : continue
                if(self.rumor[j] >= len(self.maps[j])/2) : self.counts[j] = min(next_c,self.counts[j])
                if(self.counts[j] != N+10) : next_c = max(next_c,self.counts[j])
            for j in self.maps[next]:
                # 방문하지 않았으며 소문을 퍼뜨릴 준비가 돼있어야 함. 
                if((self.check[j] == 0) & (self.rumor[j] >= len(self.maps[j])/2)) : self.queue.append((j,next_c))
    
    def last_check(self):
        for i in range(1,self.N+1):
            if(N+10 == self.counts[i]):
                self.counts[i] = -1
    
    def print_counts(self):
        for i in self.counts[1:]:
            print(i,end=" ")
        print("")
            
N = int(input())
demo = Graph(N)
for i in range(1,N+1):
    infos = list(map(int,input().split()))
    demo.set(infos,i)
M = int(input())
M_s = list(map(int,input().split()))
demo.BFS(M_s)
demo.last_check()
demo.print_counts()
