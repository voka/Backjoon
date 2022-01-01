N = int(input())
NUM_List = list(map(int,input().split()))
DP = [1] * N
numbers = []
for i in range(N):
    for j in range(i):
            if NUM_List[j] < NUM_List[i]:
                DP[i] = max(DP[i],DP[j]+1)
# Back Trace
DP.reverse() # 뒤집고
start = DP.index(max(DP)) # 최대값 찾아서 
#print(start,DP)
numbers.append(NUM_List[N-start-1])# 시작점으로 등록
cur = start# 현재 인덱스를 시작점으로
for i in range(start+1,N):
    if DP[cur] - DP[i] == 1: # 현재 인덱스와 차이가 1이나면
        #print(cur,i)
        numbers.append(NUM_List[N-i-1]) # 결과에 등록
        cur = i
numbers.reverse()
print(max(DP))
for i in numbers:
    print(i,end = " ")
    