from sys import stdin 
n = int(stdin.readline())

dp_max = [0]*(3)
temp_max = [0]*(3)
dp_min = [0]*(3)
temp_min = [0]*(3)

for i in range(n):
    f,s,t = list(map(int,stdin.readline().split()))
    for j in range(3):
        if(j == 0):
            temp_max[j] = f + max(dp_max[j],dp_max[j+1])
            temp_min[j] = f + min(dp_min[j],dp_min[j+1])

        elif(j == 1):
            temp_max[j] = s + max(dp_max[j],dp_max[j-1],dp_max[j+1])
            temp_min[j] = s + min(dp_min[j],dp_min[j-1],dp_min[j+1])
        else:
            temp_max[j] = t + max(dp_max[j],dp_max[j-1])
            temp_min[j] = t + min(dp_min[j],dp_min[j-1])
    dp_max = temp_max[:]
    dp_min = temp_min[:]    
print(max(dp_max), end=" ")
print(min(dp_min))

"""
1 2 3
1 2 3
1 2 3

1 3 6
2 6 6 + 6 + 3 -3 =
3 9 6 + 9 + 3 - 6      
"""