from sys import stdin 
strs = stdin.readline().strip()
pack_0 = 0
pack_1 = 0
for i in range(1,len(strs)):
    if strs[i-1] < strs[i]:
        pack_0 += 1
        #print(strs[i-1],strs[i])
    elif strs[i] < strs[i-1]:
        pack_1 += 1
        #print(strs[i-1],strs[i])
print(max(pack_0,pack_1))