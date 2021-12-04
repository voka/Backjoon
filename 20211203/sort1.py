def solution(array, commands):
    answer = []
    for i in commands:
        a,b,c = i
        k = array[a-1:b]
        k.sort()
        answer.append(k[c-1])
    return answer