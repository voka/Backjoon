
N,M = map(int,input().split())
temp = [0] + list(map(int,input().split()))
def nun_gulargayu(index, nun, sigan):
    global answer
    if sigan > M: #시간초과 시 빠구
        return 
    if sigan <= M: # 시간초과 안나면 비교후 정렬
        answer = max(answer, nun)
    
    if index <= N-1:
        nun_gulargayu(index+1, nun+temp[index+1],sigan+1) # 한칸 굴러갈때
    if index <= N-2:
        nun_gulargayu(index+2, nun//2+temp[index+2],sigan+1) # 두칸 굴러갈때
    
answer = 0
nun_gulargayu(0,1,0)
print(answer)