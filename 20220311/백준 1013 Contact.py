import sys,re
ip = sys.stdin.readline
out = sys.stdout.write
N = int(ip())
pattern = "(100+1+|01)+"
M = re.compile(pattern)
for i in range(N):
    Request = ip().rstrip()
    fm = M.fullmatch(Request)  
    out("YES\n" if fm else "NO\n")
