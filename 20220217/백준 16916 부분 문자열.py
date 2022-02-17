import sys
S = sys.stdin.readline().strip()
S_len = len(S)
P = sys.stdin.readline().strip()
P_len = len(P)
def makePatternTable(): # 접두사 접미사 테이블 만들기 
    mytable = [0 for _ in range(P_len)]
    j = 0
    for i in range(1,P_len):
        while(j>0 and P[i] != P[j]):
            j = mytable[j-1]
        if P[i] == P[j]:
            j += 1
            mytable[i] = j
    return mytable 
def KMP():
    Pattern_Table = makePatternTable()
    j = 0
    for i in range(S_len):
        while j > 0 and S[i] != P[j]: # 일치하지 않았을때는 이전 값까지의 최대 일치 길이를 반봔한다.
            j = Pattern_Table[j-1] # 접두사의 길이만큼 반복을 줄이는 것 
        if S[i] == P[j] :
            if j == P_len - 1:
                print(1)
                return 
            else:
                j += 1
    print(0)
    return 
KMP()
        
    