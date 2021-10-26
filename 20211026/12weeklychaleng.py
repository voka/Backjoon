import itertools

def solution(k, dungeons):
    answer = -1
    alpha = [i for i in range(len(dungeons))]
    alpha = list(itertools.permutations(alpha))
    for arr in alpha:
        temp = k
        temp_ans = 0
        for i in arr:
            if(dungeons[i][0] <= temp):
                temp = temp - dungeons[i][1]
                temp_ans += 1
        answer = max(temp_ans,answer)

    return answer

