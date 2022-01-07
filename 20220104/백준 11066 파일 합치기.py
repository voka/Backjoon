from sys import stdin 
import math
def main():
    # 점화식 
    # number[i][j] = min(number[i][j], number[i][k] + number[k+1][j])
    dp = []
    N = int(stdin.readline())
    num_list = list(map(int,stdin.readline().split()))
    number = [[0]*N for _ in range(N)]
    for i in range(N-1):
        number[i][i+1] = num_list[i] + num_list[i+1]
        for j in range(i+2,N):
            number[i][j] = number[i][j-1] + num_list[j]
    
    for dis in range(2,N):
        for i in range(N-dis):
            j = i+dis
            mins = [number[i][k] + number[k+1][j] for k in range(i,j)]
            number[i][j] += min(mins)
    print(number[0][N-1])
    print(number)
        
        
        
            
            
T = int(stdin.readline())
for _ in range(T) : main()