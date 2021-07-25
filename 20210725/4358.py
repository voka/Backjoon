import sys

lines = sys.stdin.readline
num = 0
md = {}
while True:
    line = lines().rstrip()
    if not line:
        break
    if line in md:
        md[line] = md[line] + 1
    else:
        md[line] = 1
    num+=1
md = sorted(md.items())
for i in md:
    print('%s %.4f' %(i[0],i[1]/num*100))
