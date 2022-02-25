import sys
ip = sys.stdin.readline
temps = []
answer = []
max_len = 0
for i in range(5):
    tmp = ip().strip()
    temps.append(tmp)
    max_len = max(max_len,len(tmp))
for j in range(max_len):
    for i in range(5):
        if len(temps[i]) > j :
            answer.append(temps[i][j])
#print(answer)
print("".join(answer))