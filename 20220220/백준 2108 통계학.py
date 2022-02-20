import sys,math
ip = sys.stdin.readline
N = int(ip())
num_list = []
mydict = {}
for i in range(N):
    cur = int(ip())
    num_list.append(cur)
    if cur in mydict:
        mydict[cur] += 1
    else:
        mydict[cur] = 1 
num_list.sort()
print(round(sum(num_list)/N))
print(num_list[N//2])
K = sorted(mydict.items(), key = lambda x : (-x[1],x[0]))
if len(K) == 1:
    print(K[0][0])
elif K[0][1] == K[1][1]:
    print(K[1][0])
else:
    print(K[0][0])
print(num_list[-1] - num_list[0])