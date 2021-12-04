from functools import cmp_to_key

def xy_compare(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1
        
    
def solution(numbers):
    k = []
    answer = ''
    for i in numbers:
        k.append(str(i))
    k.sort(key=cmp_to_key(xy_compare))
    if k[0] == '0':
        answer = '0'
    else:
        answer = ''.join(k)
    return answer