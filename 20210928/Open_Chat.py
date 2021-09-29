def solution(record):
    Mydict = {}
    Mylist = []
    for s in record : 
        s_list =  s.split(" ")
        flag = s_list[0]
        ID = s_list[1]
        if(flag == 'Enter'):
            NAME = s_list[-1]
            Mydict[ID] = NAME  
            Mylist.append([ID,"ENTER"])  
        elif(flag == 'Leave'):
            Mylist.append([ID,"LEAVE"]) 
        else:
            NAME = s_list[-1]
            Mydict[ID] = NAME
    answer = []
    #print(Mylist,Mydict)
    for i in Mylist:
        plus_s = ""
        if(i[1] == "ENTER"):
            plus_s = f"{Mydict[i[0]]}님이 들어왔습니다."
        else:
            plus_s = f"{Mydict[i[0]]}님이 나갔습니다."
        answer.append(plus_s)
    
    return answer