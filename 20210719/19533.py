T = int(input())
while(T):
    T -= 1
    answer = ""
    a,b = map(int,input().split())
    odd = "1-3-5-7-10-13-16-..."
    even = "-2-4-6-8-11-14-17..."
    if(a & 1):
        if(b > 2 | a > 17):
            print(odd)
        else:
            Len_answer = a*(10**b)
            print(odd[:Len_answer])
    else:
        
        if(b > 2 | a > 17):
            print(even)
        else:
            Len_answer = a*(10**b)
            print(even[:Len_answer])
