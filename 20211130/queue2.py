def solution(priorities, location):
    answer = 0
    orders = [i for i in range(len(priorities))]
    while True:
        cur_priorty = priorities.pop(0)
        cur_orders = orders.pop(0)
        flag = 0
        for i in priorities:
            if cur_priorty < i :
                priorities.append(cur_priorty)
                orders.append(cur_orders)
                flag = 1
                break
        if flag == 0 :
            answer += 1
        if((cur_orders == location) & (flag == 0)):
            break
            
    return answer