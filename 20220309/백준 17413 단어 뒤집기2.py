import re,sys

mystr = sys.stdin.readline().rstrip()
checkstr = "[<*>]"
result = re.finditer(checkstr, mystr)
i = 0
start = []
end = []
for r in result:
    if i % 2 == 0:
        start.append(r.span()[0])
    else:
        end.append(r.span()[0])
    i += 1
answer = []
def split_reverse(tmp):
    result = []
    lst = list(tmp.split())
    for t in lst:
        result.append(reverse_str(t))
    return " ".join(result)

def reverse_str(s):
    t = list(s)
    t.reverse()
    return "".join(t)


if len(start) == 0:
    print(split_reverse(mystr))
else:
    for j in range(len(end)):
        if j == 0 :
            if start[j]!= 0 :
                answer.append(split_reverse(mystr[:start[j]]))
        else:
            answer.append(split_reverse(mystr[end[j-1]+1:start[j]]))
        answer.append(mystr[start[j]:end[j]+1])
    if end[-1] != len(mystr)-1:
        answer.append(split_reverse(mystr[end[-1]+1:]))
    print("".join(answer))