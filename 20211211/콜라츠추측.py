def solution(num):
    answer = 0
    enum = 0
    while True:
        if(num == 1):
            break
        if(enum > 500):
            answer = -1
            break
        if(num&1):
            num = num * 3 + 1
        else:
            num = int(num / 2)
        enum += 1
    if(enum < 500):
        answer = enum
    return answer
