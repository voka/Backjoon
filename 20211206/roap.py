N = int(input())
roap_list = []
for i in range(N):
    k = int(input())
    roap_list.append(k)
roap_list.sort(reverse=True)
list_roap = []
num = 1
for i in roap_list:
    list_roap.append(i*num)
    num += 1
print(max(list_roap))
    
    