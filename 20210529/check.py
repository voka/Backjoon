
f = open('input.txt', mode='r', encoding='utf-8')
f2 = open('out.txt', mode='r', encoding='utf-8')
N = int(f.readline())
l = []
answer = []
for i in range(N):
    answer.append(int(f.readline()))
for i in range(N):
    l.append(int(f2.readline()))
answer.sort()
if(answer == l):
    print("correct")
else:
    print("Wrong_answer")
