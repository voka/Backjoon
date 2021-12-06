N = input()
num_list_N = list(map(int,input().split()))
num_Dict = {}
for i in num_list_N:
    if i in num_Dict:
        num_Dict[i] += 1
    else:
        num_Dict[i] = 1
M = input()
num_list_M = list(map(int,input().split()))
for i in num_list_M:
    if i in num_Dict:
        print(num_Dict[i],end=" ")
    else:
        print(0,end=" ")