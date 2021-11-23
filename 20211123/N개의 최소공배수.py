def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm(x,y):
    return x*y // gcd(x,y)

def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = lcm(answer,arr[i])
    return answer