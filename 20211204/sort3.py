def solution(citations):
    citations.sort()
    answer = 0
    for i in range(len(citations)):
        H = len(citations)-i
        if(H <= citations[i]):
            answer = H
            break
        
    return answer