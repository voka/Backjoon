import sys,re
ip = sys.stdin.readline 
pt = sys.stdout.write 
pattern = "[A-F]?A+F+C+[A-F]?"
MC = re.compile(pattern)
N = int(ip())
for i in range(N):
    check = ip().rstrip()
    result = MC.fullmatch(check)
    pt("Infected!\n" if result else "Good\n")