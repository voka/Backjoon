import sys 
ip = sys.stdin.readline
N = int(ip())
scores = [int(ip()) for _ in range(N)]
answer = 0
for i in range(N-2,-1,-1):
    tmp = scores[i+1] - (scores[i]+1)
    if tmp < 0 :
        answer += -tmp
        scores[i] = scores[i+1] - 1

#print(scores)
print(answer)

# 50 40 30 60 5
        