#import pprint 
Dates,num_K = map(int,input().split())
maximum = num_K - int(num_K/Dates) + 1 # Dates-1 에 들어갈 수 있는 떡 개수 
for i in range(maximum,-1,-1):
    fibo = [-1]*(Dates+1)
    fibo[Dates] = num_K
    fibo[Dates-1] = i
    # 피보나치 수열인데 뒤 D-2값이 D-1 값보다 크면 D-3값은 음수가 되므로 여기서부터는 탈락 
    if fibo[Dates] - fibo[Dates-1] > fibo[Dates-1]: 
        break
    for j in range(Dates,2,-1):
        fibo[j-2] =  fibo[j] - fibo[j-1] # 수열 채우기
        if fibo[j-2] < 0 :
            break
    if fibo[1] > 0: # 맨 처음값이 0보다 크면 통과
        #pprint.pprint(fibo)
        print(fibo[1])
        print(fibo[2])
        break
