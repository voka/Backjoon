
N = int(input())
line = map(int,input().split())
answer = [0 for i in range(11)]
count = 1
for i in line:
    left = i
    index = 0
    while(1):
        if(answer[index] == 0 and left == 0):
            answer[index] = count;
            count += 1
            break
        elif(answer[index] == 0):
            left -= 1
        index += 1

for i in answer:
    if(i == 0):
        break
    else:
        print(i,end=' ')