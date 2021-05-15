T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    temp = a % 10
    one_list = []
    one_list.append(temp)
    a_ = a*a
    while 1 :
        temp_ = a_%10
        if(temp_ == temp):
            break
        else:
            one_list.append(temp_)
        a_ = temp_ * a
    if(len(one_list) == 0):
        if(one_list[0] == 0):
            print(10)
        else:
            print(one_list[0])
    else:
        index = b%(len(one_list)) - 1
        if one_list[index] == 0:
            print(10)
        else:
            print(one_list[index])

    
