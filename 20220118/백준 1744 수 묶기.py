from sys import stdin 
from queue import PriorityQueue # 자연수는 큰수, 음수는 작은수 끼리 서로 곱해야 하므로 우선순위큐 사용 -> 정렬로 해도 된다. 
N = int(stdin.readline())
minus = PriorityQueue() # 음수 + 0 을 담을 공간
plus = PriorityQueue() # 자연수를 담을 공간
for i in range(N):
    cur = int(stdin.readline())
    if cur > 0 :
        plus.put(-1*cur) # 큰수부터 나오게 하기 위해 -1을 곱한다. 
    else:
        minus.put(cur)
last = 0
plus_answer = 0 # 자연수 정답
while not plus.empty():  
    last = -1*plus.get()
    if not plus.empty(): # 수 두개를 뽑을 수 있다면 
        cur = -1*plus.get() 
        plus_answer += max(last*cur,last + cur) # 한 숫자가 1인 경우에는 더하는 값이 곱하는 값보다 크다. 
        last = 0 # 이때 큐가 빈다면 last는 0이어야지 정답에 영향을 주지 않는다. 
    else:
        break
plus_answer += last
last = 0
minus_answer = 0 #음수 정답 
while not minus.empty():
    last = minus.get()
    if not minus.empty():
        cur = minus.get()
        minus_answer += last*cur # 제일 큰 숫자는 0인데 음수 한개가 남고 0이 남았더면 두개를 곱하는 것이 최대 값이 된다. 
        # 그래서 자연수 부분과 다르게 Max함수를 사용하지 않는다. 
        last = 0 # 이때 큐가 빈다면 last는 0이어야지 정답에 영향을 주지 않는다. 
    else:
        break
minus_answer += last
#print(minus_answer,plus_answer)
print(plus_answer + minus_answer)