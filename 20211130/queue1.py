def solution(progresses, speeds):
    answer = []
    tt = len(speeds)
    cur_p = progresses.pop(0)
    cur_s = speeds.pop(0)
    total_num = 0
    while total_num < tt:
        cur_p += cur_s
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        if(cur_p >= 100):
            i = 0
            while True:
                if len(speeds) == 0 :
                    break
                if(progresses[0] >= 100):
                    progresses.pop(0)
                    speeds.pop(0)
                    i += 1
                else:
                    cur_p = progresses.pop(0)
                    cur_s = speeds.pop(0)
                    break
            total_num += i + 1 
            answer.append(i+1)     
        
    return answer