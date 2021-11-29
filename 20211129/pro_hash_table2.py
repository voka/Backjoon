def solution(clothes):
    mylook = {}
    for i in clothes:
        if i[1] in mylook:
            mylook[i[1]] += 1
        else:
            mylook[i[1]] = 1
    
  
    answer = 1
    for i in mylook.values():
        answer = answer * (i+1)
            
    return answer - 1