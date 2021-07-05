my_str = list(input())
boom = list(input())
bs = len(boom)
stack = []
for i in range(len(my_str)):
    stack.append(my_str[i])
    if(len(stack) >= bs):
        if boom == stack[-bs:]:
            cnt = 0
            while cnt < len(boom):
                stack.pop()
                cnt += 1
if len(stack) == 0 : print("FRULA")
else : print("".join(stack))