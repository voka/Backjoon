T = 3
while(T):
    T-=1
    temp = [0 for i in range(10)]
    answer = 0
    my_str = list(input())
    for i in my_str:
        i = int(i)
        if(temp[i] != 0 and pre != i):
            temp[i] = 0
        pre = i
        temp[i] += 1
        answer = max(answer,max(temp))
    print(answer)

