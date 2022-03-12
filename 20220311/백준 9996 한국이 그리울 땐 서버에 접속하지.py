import sys,re
ip = sys.stdin.readline 
out = sys.stdout.write
N = int(ip())
pattern = ip().rstrip().replace("*",".*")

M = re.compile(pattern)
for i in range(N):
    checkstr =ip().rstrip()
    result = M.fullmatch(checkstr)
    out("DA\n" if result else "NE\n")