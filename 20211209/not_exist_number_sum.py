def solution(numbers):
    answer = 0
    mydict = {}
    for i in numbers:
        mydict[i] = 1
    for i in range(10):
        if i in mydict:
            pass
        else :
            answer += i
    return answer