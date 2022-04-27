import sys
ip = sys.stdin.readline
ins,outs = [],[]
for j in range(4):
  o,i = map(int,ip().split())
  ins.append(i)
  outs.append(o)
cur, answer = 0,0
for i in range(4):
  cur += ins[i] - outs[i]
  answer = max(answer,cur)
print(answer)
