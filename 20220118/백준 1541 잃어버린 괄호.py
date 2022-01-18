from sys import stdin
expression = stdin.readline().strip()
minus_id = []
MyE = []
N = len(expression)
pre = 0
for i in range(N): # 0으로 시작하는 수 변환
    if expression[i] == '+' or expression[i] == '-':
        MyE.append(str(int(expression[pre:i])))
        if expression[i] == '-': minus_id.append(len(MyE))
        MyE.append(expression[i])
        pre = i+1
    if i == N-1 :
        MyE.append(str(int(expression[pre:i+1])))
final_ans = []
pre = 0
for i in range(len(MyE)): # - 없는 부분만 먼저 계산 
    #print("".join(MyE[pre:i]))
    if i in minus_id:
        final_ans.append(str(eval("".join(MyE[pre:i]))))
        final_ans.append(MyE[i])
        pre = i+1
    if i == len(MyE) - 1:
        final_ans.append(str(eval("".join(MyE[pre:i+1]))))

print(eval("".join(final_ans)))
