import sys, pprint
maps = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if maps[i][j] == 0:
           zero.append((i,j)) 
fillnum = len(zero)

def Check_Row(x,a): # x번째 행에 a라는 숫자가 있는지 확인
    for i in range(9):
        if a == maps[x][i]:
            return False
    return True

def Check_Col(x,a): # x번째 열에 a라는 숫자가 있는지 확인
    for i in range(9):
        if a == maps[i][x]:
            return False
    return True

def Check_Rect(x,y,a): # x,y 가 속한 3X3정사각형 내부에 해당 번호가 있는지 확인 
    start_x = x//3*3
    start_y = y//3*3
    for i in range(3):
        for j in range(3):
            if a == maps[start_x+i][start_y+j]:
                return False
    return True

def DFS(x): # x는 채운 0의 개수
    if x == fillnum:
        for i in range(9):
            print(*maps[i])
        exit(0)
    for i in range(1,10): # 1부터 9까지의 숫자이므로
        cur_x,cur_y = zero[x]
        #print(cur_x,cur_y)
        if Check_Col(cur_y,i) and Check_Row(cur_x,i) and Check_Rect(cur_x,cur_y,i):
            maps[cur_x][cur_y] = i
            DFS(x+1)
            maps[cur_x][cur_y] = 0
#print(fillnum)
DFS(0)