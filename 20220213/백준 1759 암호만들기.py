import sys
from itertools import combinations
checkList = ['a','e','i','o','u']
L,C = map(int,sys.stdin.readline().split())
mystr = list(sys.stdin.readline().split())
mo = [] # 모음 배열
ja = [] # 자음 배열
for m in mystr:
    if m in checkList:
        mo.append(m)
    else:
        ja.append(m)
#print(mo,ja,len(mo),len(ja))
possible = []
for i in range(1,len(mo)+1): # 모음은 한개이상이고 자음은 두개 이상이므로 모음을 기준으로 반복문 실행 
    m_num = i # 모음 개수 --> 1개 이상
    ja_num = L - i # 자음 개수 --> 전체 - 모음개수
    #print(m_num,ja_num)
    if ja_num < 2: # 자음개수가 2개 이상이 안되면 Stop
        break
    m = list(combinations(mo,m_num)) # 모음 조합 구하기
    j = list(combinations(ja,ja_num)) # 자음 조합 구하기
    for a in m:
        for b in j:
            #print(a,b)
            temp = list(a)
            temp.extend(list(b))
            temp.sort() # 알파벳 순서로 정렬하고 
            k = ''.join(temp) # 합쳐서 
            possible.append(k) # 넣는다.
possible.sort() # 모여진 알파벳을 정렬하고
for p in possible: #출력한다. 
    print(p)