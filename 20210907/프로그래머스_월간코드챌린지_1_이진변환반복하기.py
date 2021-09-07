def solution(s):
    num = 0
    c=0
    while(s != "1"):
        n,s = remove_zero(s)
        num += n
        c = c + 1
    answer = [c,num]
    return answer

def remove_zero(s):
    num = s.count('0')
    s = s.replace('0','')
    s = str(bin(s.count('1'))[2:])
    return num,s
    
def len_of_string(s):
    r = len(s)
    ret = ""
    while(int(r) > 0):
        ret = str(int(r)%2) + ret
        r = r/2
    return ret
"""
len_of_string 요거 대신에 
str(bin(s.count('1'))[2:]) 요거 써도 될듯  <- 문자열 s 중에 1인 문자의 개수를 세서 10진수를 2진수로 변환한 다음 str로 감싸서 문자열로 만듬.

"""
