import sys
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
answer = 0

while True:
    if S == T:
        answer = 1
        break
    if len(S) > len(T):
        break
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[::-1]
        T = T[1:]
    else:
        break
print(answer)
        
    
    
    
    