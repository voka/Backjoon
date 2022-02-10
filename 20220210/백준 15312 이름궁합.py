import sys
from collections import deque
from string import ascii_uppercase
alpha_list = list(ascii_uppercase)
num_list = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
mydict = {}
for i in range(len(num_list)):
    mydict[alpha_list[i]] = num_list[i]
#print(mydict)
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
cur = deque()
for i in range(len(a)):
    cur.append(mydict[a[i]])
    cur.append(mydict[b[i]])
#print(cur)
answer = 0
while True:
    cur_max = len(cur)
    for i in range(cur_max):
        a = cur.popleft()
        b = cur.popleft()
        cur.appendleft(b)
        cur.append((a+b)%10)
    cur.pop()
    #print(cur)
    if len(cur) == 2:
        break
    
print(cur[0],end="")
print(cur[1])
    
