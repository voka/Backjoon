import sys,math
ip = sys.stdin.readline
N = int(ip())
N_List = list(map(int,ip().split()))
N_List.sort()
cur_min = math.inf
answers = [0]*3
for s in range(N-2): # s 를 고정시켜두고 i 와 j 를 이용해 투 포인터 탐색을 시작한다. --> i가 j보다 작을때 까지만 
    i = s + 1
    j = N-1
    pre = math.inf
    while i < j:
        cur = N_List[s] + N_List[i] + N_List[j] # 3개를 더한다
        if cur == 0 : # 이때 모두 더해서 0인 경우가 있다면 바로 출력하고 프로그램을 종료한다. 
            print(N_List[s],N_List[i],N_List[j])
            exit()
        if cur_min > abs(cur): # 최선으로 구한 min과 현재의 절댓값을 비교해 현재 절댓값이 더 작다면 수를 교체한다.   
            cur_min = abs(cur)
            answers[0] = N_List[s]
            answers[1] = N_List[i]
            answers[2] = N_List[j]
        if cur < 0: # cur이 음수라면 i가 증가하면서 0에 가깝도록 수를 키우고 
            i += 1
        else:# cur이 양수라면 j가 감소하면서 0에 가깝도록 조정한다. 
            j -= 1
print(*answers)