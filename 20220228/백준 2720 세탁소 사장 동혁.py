import sys
ip = sys.stdin.readline
N = int(ip())
for i in range(N):
    answer = []
    C = int(ip())
    Somes = [25,10,5,1]
    for j in range(4):
        temp = C // Somes[j]
        C -= Somes[j]*temp
        answer.append(temp)
    print(*answer)