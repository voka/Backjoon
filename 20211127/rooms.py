
# n , k , result
# 5  12	  [4,4] 
# 5  16	  [1,2]
# 6  13	  [4,5]
class room():
    def __init__(self,n,k):
        bench = [ 0 for i in range(n)]
        self.room = [bench for i in range(n)]
        self.calroom = [bench for i in range(n)]
        self.dx = [1,-1,0,0]
        self.dy = [0,0,1,-1]
        self.n = n
        self.k = k
    def setting_123(self):
        self.room[0][0] = 1
        self.bfs(0,0,1)
        #self.calroom[0][0] = 0
        self.room[-1][-1] = 2
        #self.calroom[-1][-1] = 0
        self.room[0][-1] = 3
        #self.calroom[0][-1] = 0
            
    def insert_num(self,x,y):
        pass
    def bfs(self,x,y,cnt):
        """
        if calroom[x][y] == 0:
            return 
        if calroom[x][y] == 1:
            if flag == 1:
                calroom[x][y] = 0
                return
        """
        for i in range(4):
            next_x = x + self.dx[i]
            next_y = y + self.dy[i]
            if(next_x > self.n or next_x < 0) :
                continue
            if(next_y > self.n or next_y < 0) :
                continue
            if(self.room[next_x][next_y] != 0):
                continue
            if(self.calroom[x][y] > self.calroom[next_x][next_y]):
                continue
            self.calroom[next_x][next_y] = cnt
            cnt += 1
            self.bfs(next_x,next_y,cnt)
            
        

def solution(n, k):
    myroom = room(n,k)
    myroom.setting_123()
    for i in myroom.calroom:
        print(i)
        
    
solution(10,10)


# BFS 공부 다시 할 것 !!1