import sys,pprint,math
from collections import deque
mystr = sys.stdin.readline().strip()
lens = len(mystr)
mydp = [[0 for i in range(lens)] for _ in range(lens)] # mydp[Start][End] : Start 인덱스 부터 End 인덱스 까지는 부분 펠린드롬 문자열이다. 
for i in range(lens):
    mydp[i][i] = 1 # 각 자리 는 모두 펠린드롬이다 -> ABC => 'A', 'B', 'C'
for i in range(lens-1):
    if mystr[i] == mystr[i+1] : # 연속된 숫자도 모두 펠린드롬이다. 
        mydp[i][i+1] = 1 # AAA -> 'AAA'
for i in range(lens): # 나머지가 펠린드롬이 되려면 
    for S in range(lens-1): # 반복문을 끝까지 돌리지 않아도 되는 이유가 이미 앞에서 각 자리수를 1로 설정해놨기 때문 
        K = i + S 
        if K < lens:
            if mystr[S] == mystr[K] and mydp[S+1][K-1]:
                mydp[S][K] = 1
answer = [0 for _ in range(lens+1)]
for Ends in range(lens):
    answer[Ends] = 2501
    for starts in range(0,Ends+1):
        if mydp[starts][Ends]:
            if starts == 0:
                answer[Ends] = 1
            else:
                answer[Ends] = min(answer[Ends],answer[starts-1]+1)
#pprint.pprint(mydp)    
#pprint.pprint(answer)
print(answer[lens-1])
