
T = int(input())
for t in range(T) : 
    data_size = int(input())
    data = list(map(int,input().split()))
    s_d = sorted(data)
    print(s_d)
    while(data_size != 2):
        temp = []
        data_size = int(data_size / 2)
        for i in range(data_size):
            t = s_d[i]+s_d[-i-1]
            print(s_d[i],s_d[-i-1])
            #if((data_size&1) and (i == data_size) ):
            #    t = s_d[data_size]
            temp.append(t)
            
        if(data_size&1) == 1:
            temp.append(s_d[data_size])
            data_size += 1
        s_d = sorted(temp)
        print("data_size == ", data_size)
        print(sum(s_d))