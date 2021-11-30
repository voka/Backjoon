def solution(prices):
    num = len(prices)
    answer = [1 for i in range(num)]
    for i in range(num-1):
        for j in range(i+1,num-1):
            if(prices[i] > prices[j]):
                break
            else:
                answer[i] += 1
    answer[-1] = 0    
    return answer