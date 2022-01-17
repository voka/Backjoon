from sys import stdin 

N = int(stdin.readline())
Mdic = {}
for i in range(N):
    k = int(stdin.readline())
    if k in Mdic:
        Mdic[k] += 1
    else:
        Mdic[k] = 1
answers = sorted(Mdic.items(), key = lambda x : (-x[1],x[0])) # Multiple key sort 
print(answers[0][0])