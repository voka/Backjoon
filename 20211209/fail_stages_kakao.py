def solution(N, stages):
    answer = []
    total_num = len(stages)
    mydict = {}
    for i in stages: # stages에 머물고 있는 사람 수 dict로 정리
        mydict[i] = mydict[i] + 1 if i in mydict else  1
    pre = 0 # total_num 에서 뺄 전 스테이지에 머문 사람 수 
    for i in range(1,N+1):
        if i in mydict : 
            pre = mydict[i]
        mydict[i] = mydict[i] / total_num if i in mydict else 0 # 스테이지에 머문 사람이 있으면 앞 스테이지에 있는 사람을 제외하고 나누기
        total_num = total_num - pre # 전 스테이지 인원인 빼준다.
        pre = 0
        
    if N+1 in stages:
        del mydict[N+1] #  최종 스테이지까지 통과한 사람은 뺀다.
        
    k = sorted(mydict.items(), key = lambda x : (-x[1],x[0])) # 실패율이 높은 스테이지가 앞쪽, 실패율이 동일하다면 스테이지 번호가 빠른 것이 앞쪽에 오도록 정렬
    for i in k: 
        answer.append(i[0]) # 스테이지 번호 담기 
        
    return answer