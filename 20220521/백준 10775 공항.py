import sys 
ip = sys.stdin.readline 

G = int(ip())
P = int(ip())
parents = [i for i in range(G+1)]
def find_parent(x):
  if parents[x] != x:
    parents[x] = find_parent(parents[x])
  return parents[x]

def union_parent(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b :
    parents[b] = a  
  else:
    parents[a] = b 
answer = 0
for i in range(1,P+1):
  g = int(ip())
  dork = find_parent(g)
  if dork != 0:
    union_parent(dork,dork-1)
    answer += 1
  else:
    break

print(answer)