def solution(phone_book):
    
    mybook = {}
    
    flag = True
    for i in phone_book:
        mybook[i] = 1
    for j in phone_book:
        for k in range(len(j)-1):
            if j[:k+1] in mybook:
                flag = False
                break
    answer = flag
    return answer