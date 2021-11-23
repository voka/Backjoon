def solution(s):
    mystack = []
    for i in s:
        if(len(mystack) == 0) : mystack.append(i)
        elif( mystack[-1] == i ) : mystack.pop() #stack 맨위에 꺼랑 배열원소 비교
        else : mystack.append(i)
    # 스택이 비어있다면 문자열 제거가 완료된 것 
    if(len(mystack) == 0) : return 1
    else : return 0