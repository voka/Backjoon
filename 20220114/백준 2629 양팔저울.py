from sys import stdin 
Nc = int(stdin.readline())
chus = list(map(int,stdin.readline().split()))
Nq = int(stdin.readline())
Questions = list(map(int,stdin.readline().split()))
dp_weights = [[0]*(40001) for _ in range(Nc+1)]
def checking(cur,x):
    if x > Nc or cur > 40000:
        return 
    if dp_weights[x][cur]:
        return 
    
    dp_weights[x][cur] = 1
    checking(abs(cur-chus[x-1]),x+1) # 추의 무게 -
    checking(cur+chus[x-1],x+1)  # 추의 무게 + 
    checking(cur,x+1) # 아무것도 안함 ㅇ 
checking(0,0)
#print(dp_weights[Nc])   
answers = []
for Q in Questions:
    if dp_weights[Nc][Q]:
        answers.append("Y")
    else:
        answers.append("N")
print(*answers)
