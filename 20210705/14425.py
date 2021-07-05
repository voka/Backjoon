N, M = map(int,input().split())
my_set = set()
check_set = []
for i in range(0,N):
    my_set.add(input())
for i in range(0,M):
    check_set.append(input())
count = 0
for i in check_set:
    if i in my_set:
        count+=1
print(count) 