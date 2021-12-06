# 조건 -> 0이 한개 이상 존재, 각 자리수를 더했을 때 3으로 나누어 떨어 져야 함.
numstr = list(input())
numstr.sort(reverse=True)
f = False
temp = 0
for i in numstr:
    cur = int(i)
    temp += cur
    if(cur == 0): f = True
if f == True and temp%3 == 0 :
    print("".join(numstr))
else:
    print(-1)