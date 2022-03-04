N = 1000 - int(input())
dongs = [500,100,50,10,5,1]
answer = 0
for i in range(6):
    cur = N // dongs[i]
    answer += cur
    N -= cur*dongs[i]
print(answer)