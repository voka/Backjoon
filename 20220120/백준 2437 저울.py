from sys import stdin
N = int(stdin.readline().strip())
weights = list(map(int,stdin.readline().strip().split()))
weights.sort()
answer = 0
# 정렬후 answer이 이제까지의 추의 합보다 크거나 같으면 추의 무게를 더하고 
# 작으면  정답이 된다. -> 아이디어 떠올리기가 힘든 문제 .. 
for i in range(N):
    if answer + 1 >= weights[i]:
        answer += weights[i]
    else:
        break
print(answer+1)
""" 계속 시간초과가 나서 결국 구글링을 했다. 
def experiance(x,w): 
    possible[w] = 1
    print(w)
    if x == N :
        return
    experiance(x+1,w+weights[x])# 추를 올린다
    experiance(x+1,w)# 추를 올리지 않는다. 

experiance(0,0)
for i in range(sum(weights)):
    if i not in possible:
        print(i)
        break
"""