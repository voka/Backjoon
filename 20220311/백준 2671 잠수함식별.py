import sys,re 
ip = sys.stdin.readline 
pt = sys.stdout.write
pattern = "(100+1+|01)+"
M = re.compile(pattern)
checkstr = ip().rstrip()
result = M.fullmatch(checkstr)
pt("SUBMARINE\n" if result else "NOISE\n") 
