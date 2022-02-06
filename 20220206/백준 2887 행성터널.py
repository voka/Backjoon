import sys,heapq

parent = [i for i in range(100001)]

def find_p(x):
    if parent[x] == x : return x
    parent[x] = find_p(parent[x])
    return (parent[x])
def Union_p(a,b):
    a = find_p(a)
    b = find_p(b)
    if a < b : parent[b] = a
    else : parent[a] = b
    
    
N = int(input())
planets_info = []
x_info = []
y_info = []
z_info = []
for i in range(N):
    x,y,z = map(int,sys.stdin.readline().split())
    x_info.append((x,i))
    y_info.append((y,i))
    z_info.append((z,i))
x_info.sort()
y_info.sort()
z_info.sort()
for i in range(1,N):
    planets_info.append((x_info[i][0] - x_info[i-1][0],x_info[i][1],x_info[i-1][1]))
    planets_info.append((y_info[i][0] - y_info[i-1][0],y_info[i][1],y_info[i-1][1]))
    planets_info.append((z_info[i][0] - z_info[i-1][0],z_info[i][1],z_info[i-1][1]))
answer = 0
planets_info.sort()
for info in planets_info:
    weight,a,b = info
    if find_p(a) != find_p(b):
        Union_p(a,b)
        answer += weight
print(answer)