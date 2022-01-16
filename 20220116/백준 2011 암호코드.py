Secret = list(map(int,input()))
l = len(Secret)
dp = [0 for _ in range(l+1)]
if (Secret[0] == 0) :
    print(0)
else : # 처음부터 숫자 확인하면서 증가시킴
    Secret.insert(0,0) # 처음자리에 0 추가해서 검사 시작 
    dp[0]=dp[1]=1
    for i in range(2, l+1):
        if Secret[i] > 0: # 한자리 검사 
            # 1~9까지는 알파벳으로 변환 가능하나 0은 변환 X 
            dp[i] += dp[i-1]
        temp = Secret[i-1] * 10 + Secret[i] # 두자리 검사할 수 만들기 
        # 1 ~ 9는 한자릿 수 검사에서 시행, 
        # 10 ~ 26까지만 두자리 숫자에서 검사 
        if temp >= 10 and temp <= 26 :
            dp[i] += dp[i-2]
        # 두자리 수 중 11 ~ 19, 21 ~ 26 같은 경우 피보나치 수열처럼 더해지게 된다.
        # 나머지인 10, 20 or 27이상인 수는 한자리수 검사에서만 더해진다. 
    print(dp)
    print(dp[l] % 1000000)
# 코드 출처 
# https://jyeonnyang2.tistory.com/55