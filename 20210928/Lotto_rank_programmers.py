def solution(lottos, win_nums):
    zero_counts = 0
    counts = 0
    high_rank = 0
    low_rank = 0
    for num in lottos:
        if num in win_nums:
            counts = counts + 1
        if num == 0:
            zero_counts = zero_counts+1
    if(counts == 0):
        low_rank = 6
        if(zero_counts == 0) : 
            high_rank = 6
        else :
            high_rank  = 7 - counts - zero_counts
    else : 
        low_rank = 7 - counts
        high_rank  = 7 - counts - zero_counts
    answer = [high_rank,low_rank]
    return answer