def sum_of_num(a):
    sum = 0
    while(1):
        if(a == 0) : return sum
        sum += a%10
        a = int(a/10) 
s = input()
for i in s:
    b = ord(i)
    print(i*sum_of_num(b))
