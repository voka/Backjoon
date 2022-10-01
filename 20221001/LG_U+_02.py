import sys

ip = sys.stdin.readline
ipstr = ip()
def find_back(start,ipstr):
    result = 0
    for s in range(start,-1,-1):
        if ipstr[s].isnumeric():
            result = s
        else:
            break
    return result


def uncompress_str(compressed):
    stack = []
    s = 1
    while True:
        if len(compressed) == s:
            break
        #print('s  ===> {}'.format(s) + ", str ===> " + compressed[s])
        if compressed[s] == "(":
            start = find_back(s-1,compressed)
            stack.append((start,s+1,int(compressed[start:s])))
        elif compressed[s] == ")":
            if len(stack) == 0:
                continue
            else:
                start,str_start,multi = stack.pop()
            end = s
            #print(start,end,multi, end+1-start, multi*(end-str_start))
            compressed = compressed.replace(compressed[start:end+1],multi*compressed[str_start:end],1)
            reduced_len = end+1-start - multi*(end-str_start)
            #print(reduced_len)
            s -= reduced_len
        s += 1
        #print(stack)
    print(compressed)
    return compressed
uncompress_str(ipstr)