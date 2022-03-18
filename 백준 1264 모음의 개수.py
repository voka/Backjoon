import sys,re
ip = sys.stdin.readline
k = re.compile("[aeiouAEIOU]")
while True:
    mystr = ip().rstrip()
    if mystr == "#":
        break
    result = k.findall(mystr)
    print(len(result))