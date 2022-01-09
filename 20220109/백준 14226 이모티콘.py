"""
1 -> 2 -> 4 -> 8 
            -> 3 -> 6 -> 12
                      -> 5 - > 10
"""
from queue import Queue
N = int(input())

clip_board = 0
myque = Queue()
myque.put((1,clip_board)) # 현재 화면의 이모티콘 수 , 클립보드의 이모티콘 수 
visited = dict()
visited[(1,0)] = 0
while not myque.empty():
    cur, clip_board = myque.get()
    if cur == N:
        print(visited[cur,clip_board])
        break
    if (cur,cur) not in visited.keys():
        visited[(cur,cur)] = visited[(cur,clip_board)] + 1
        myque.put((cur,cur))
    if (cur-1,clip_board) not in visited.keys():
        visited[(cur-1,clip_board)] = visited[(cur,clip_board)] + 1
        myque.put((cur-1,clip_board))
    if (cur+clip_board,cur) not in visited.keys():
        visited[(cur+clip_board,clip_board)] = visited[(cur,clip_board)] + 1
        myque.put((cur+clip_board,clip_board))
        
    
    
# 음... 공부를 더 해야 겠습니다. 