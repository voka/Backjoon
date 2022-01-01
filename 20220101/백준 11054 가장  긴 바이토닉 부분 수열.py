N = int(input())
NUM_List = list(map(int,input().split()))
B_DP = [1] * N
L_DP = [1] * N
for i in range(0,N,1): #  == for i in range(0,N,1) --> start, end, 증감 
    for j in range(i):
            if NUM_List[j] < NUM_List[i]:
                L_DP[i] = max(L_DP[i],L_DP[j]+1)
R_DP = [1] * N
for i in range(N,-1,-1): # --> start = N, end = -1 , 증감 = -1// end+1까지 반복문이 수행되므로 end == 0 까지가 된다.
    for j in range(N-1,i,-1):#  --> N-1 --> start, i --> end , 증감  = -1 
            if NUM_List[j] < NUM_List[i]:
                R_DP[i] = max(R_DP[i],R_DP[j]+1)

for i in range(N):
    B_DP[i] = L_DP[i] + R_DP[i]-1
print(max(B_DP))
    