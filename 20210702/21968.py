T = int(input())
two_s = [ 2**i for i in range(37)]
three_s = [ 3**i for i in range(37)]
two_s.reverse()
three_s.reverse()
def to_th(num):
    answer = 0
    for t in range(0,37):
        if(num - two_s[t] >= 0):
            num = num - two_s[t]
            answer = answer + three_s[t]
    print(answer)
while(T):
    T = T - 1
    i = int(input())
    to_th(i)
    
