import sys

def decode_daily():
    lst = ['a', 'e', 'i', 'o', 'u']
    line = sys.stdin.readline().rstrip()

    string = []
    cnt = 0
    for i in range(len(line)):
        if line[i] in lst and cnt == 0:
            string.append(line[i])
            cnt = 2
        else:
            if cnt > 0:
                cnt -= 1
                continue
            string.append(line[i])
    print(''.join(string))
decode_daily()