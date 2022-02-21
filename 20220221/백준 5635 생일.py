import sys
ip = sys.stdin.readline
N =int(ip())
lists = []
for i in range(N):
    name,Day,month,year = ip().strip().split()
    Day,month,year = int(Day),int(month),int(year)
    lists.append((name,Day,month,year))
lists.sort(key = lambda x : (x[3],x[2],x[1]))
print(lists[-1][0])
print(lists[0][0])