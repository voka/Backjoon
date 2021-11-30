def solution(bridge_length, weight, truck_weights):
    answer = 1
    cur_lens = [1]
    cur_weights = [truck_weights[0]]
    cur_weight = truck_weights.pop(0)
    while True:
        #print(cur_weights,cur_lens,answer)
        if len(cur_lens) == 0:
            break
        if(cur_lens[0] >= bridge_length):
            cur_weight -= cur_weights[0]
            cur_weights.pop(0)
            cur_lens.pop(0)
        for i in range(len(cur_lens)) :
            cur_lens[i] += 1
        if len(truck_weights) > 0:
            if cur_weight + truck_weights[0] <= weight:
                cur_weights.append(truck_weights[0])
                cur_weight += truck_weights.pop(0)
                cur_lens.append(1)
        answer += 1 
    return answer