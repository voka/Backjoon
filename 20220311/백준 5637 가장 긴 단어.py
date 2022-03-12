import sys,re,string
ip = sys.stdin.readline
max_len = 0
answer = ""
while True:
    check = ip().rstrip()
    result = re.findall(r"[a-zA-Z-]+",check)
    if result :
        for r in result:
            rl = len(r)
            if rl > max_len:
                max_len = rl
                answer = r
        if result[-1] == "E-N-D":
            break
print(answer.lower())