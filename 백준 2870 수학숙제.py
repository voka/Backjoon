import sys,re
ip = sys.stdin.readline 
N = int(ip())
find_digit = re.compile('[0-9]+')
answer = []
for i in range(N):
    mystr = ip().rstrip()
    result = find_digit.findall(mystr)
    for r in result:
        answer.append(int(r))
answer.sort()
for a in answer:
    print(a)