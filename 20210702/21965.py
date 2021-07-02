sizes = int(input())
numbers = list(map(int,input().split(" ")))

def is_mountien():
    flag = -1
    pre = numbers[0]
    id = 1
    while(1):
        if(id == sizes): break;
        if(pre < numbers[id]):
            if(flag == 1) : break
        elif(pre > numbers[id]):
            flag = 1
        else : 
            break
        pre = numbers[id]
        id = id + 1
        
    if(id != sizes):
        print("NO")
    else:
        print("YES")
is_mountien()