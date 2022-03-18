import sys
ip = sys.stdin.readline 
N = int(ip())
students = []
for i in range(1,N+1):
    students.append(int(ip()))
students.sort()
answer = 0
for s in range(1,N+1):
    answer += abs(students[s-1] - s)
print(answer)
