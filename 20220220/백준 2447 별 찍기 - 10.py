N = int(input())
def printstar(n):
    if n == 1: return ['*']
    ans = printstar(n//3)
    tmp = []
    for i in ans : tmp.append(i*3)
    for i in ans : tmp.append(i+' '*(n//3) + i)
    for i in ans : tmp.append(i*3)
    
    return tmp
print("\n".join(printstar(N)))    