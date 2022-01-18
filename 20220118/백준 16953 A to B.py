A,B = map(int,input().split())
cal = 1
while True:
    if B % 2 == 0:
        B = int(B /2)
    elif B % 10 == 1:
        B = int(B / 10) 
    else:
        break
    cal += 1
    if A >= B:
        break
#print(A,B)
if A == B:
    print(cal)
else:
    print(-1)
    