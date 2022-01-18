from sys import stdin
import math 
i = 1
while True:
    L,P,V = map(int,stdin.readline().split())
    if L == 0 and P == 0 and V == 0 :
        break
    answer = math.floor(V/P) * L
    rest = V%P
    if rest < L:
        answer += rest
    else:
        answer += L
    str_answer = "Case {0}: {1}".format(i,answer)
    print(str_answer)
    i += 1