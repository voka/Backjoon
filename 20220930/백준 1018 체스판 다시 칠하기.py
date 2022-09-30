import sys

ip = sys.stdin.readline
N,M = map(int,ip().split())

#시작 지점 찾기
def find_start_points():
    result = []
    for i in range(N-7):
        for j in range(M-7):
            result.append((i,j))
    return result

mymap = [[] for i in range(N)]
for i in range(N):
    instr = ip().strip()
    for s in range(len(instr)):
        mymap[i].append(instr[s])

#print(mymap)
starts_points = find_start_points()
#print(starts_points)
start_B = "BWBWBWBW"
start_W = "WBWBWBWB"
selist = [[start_B, start_W],[start_W,start_B]]
cur_min = 1e9 #max int

#바꿔야하는 타일 수 찾기 -> 중간에 현재 최소 타일 수 보다 작으면 break
for x,y in starts_points:
    for first,second in selist:
        count = 0
        for i in range(4):
            for j in range(8):
                if(mymap[x + 2*i][y + j] != first[j]):
                    count += 1
                if(mymap[x + 2*i+1][y + j] != second[j]):
                    count += 1
            if(count > cur_min):
                break
        if(count < cur_min):
            cur_min = count
print(cur_min)