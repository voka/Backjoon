"""
증가하다가 감소하는 부분수열 개수 찾기
input : output
[0, 1, 2, 5, 3, 7] :	3
[1, 2, 3, 2, 1] :	4
[1, 2, 3, 2, 1, 4, 3, 2, 2, 1] : 6
[1, 2, 1, 2, 1]	 : 2

"""

def solution(arr):
    flag = 1 # 증가 개수부터 시작
    pre = arr[0] # 이전값과 비교하기 위함
    answer = 0 # 정답
    ftemp = 0 # 수열에서 증가 갯수
    etemp = 0 # 수열에서 감소 갯수
    for i in range(len(arr)):
        if flag == 1 : # 증가하는 거 세고
            if(pre < arr[i]):
                ftemp += 1 # 앞쪽 증가 개수
            elif pre == arr[i]:
                ftemp = 0 # 중간에 증가가 멈추면 0으로 초기화
            else : 
                flag = -1 # 감소 flag로 이동
        if flag == -1: # 감소하는 거 세고
            if(pre > arr[i]):
                etemp += 1 # 뒷쪽 감소 개수
            else :  # 감소개수가 0이면 더해지는 값이 0이 되기 때문에 따로 Case를 두지 않는다.
                answer += ftemp * etemp # 앞쪽 개수와 뒷쪽 개수를 곱한다. 
                if(pre < arr[i]): ftemp = 1 # 이때 증가 부분 이면 ftemp를 1로 초기화
                else : ftemp = 0 # 아니라면 0으로 초기화
                etemp = 0 # 감소 개수는 0으로 초기화
                flag = 1 # 다시 증가 flag로
        #print(flag, pre,arr[i],ftemp,etemp)
        pre = arr[i]
    
    answer += ftemp * etemp        
    #print(answer)
        
    return answer