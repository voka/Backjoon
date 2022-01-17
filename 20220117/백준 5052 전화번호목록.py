from sys import stdin 

def solution():
    n = int(stdin.readline())
    num_list = []
    for j in range(n):
        numbers = (stdin.readline().strip())
        num_list.append(numbers)
    num_list.sort() #  정렬을 하기 때문에 앞, 뒤 숫자만 확인해도 모든 경우를 checking할 수 있다. 
    print(num_list)
    for i in range(n-1):
        i_len = len(num_list[i])
        if num_list[i] == num_list[i+1][0:i_len]:
            return "NO"
    return "YES"

T = int(input())
for i in range(T):
   answer = solution()
   print(answer)