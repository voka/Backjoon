#include <bits/stdc++.h>
using namespace std;
/* 
Q. 1로 만들기

- 문제 설명

· 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.

 1. X가 5로 나누어 떨어지면, 5로 나눈다.

 2. X가 3으로 나누어 떨어지면, 3으로 나눈다.

 3. X가 2로 나누어 떨어지면, 2로 나눈다.

 4. X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 한다. 
연산을 사용하는 횟수의 최솟값을 출력하라



예시1.
input :
    26
output : 
    4 
    (26-1=25 
    -> 25/5 = 5 
    -> 5/5 = 1)


풀이방법 
4가지 연산 방법이 있으므로
4가지 경우가 있을 수 있다.

dp[n] = min(dp[n-1]+1,dp[n/5]+1,dp[n/3]+1,dp[n/2]+1)로 점화식을 세울 수 있다.

그렇지만 n이 5,3,2로 나누어 떨어지는 경우에만 사용할 수 있는 식들이 있으므로
if문으로 구분해 주면 된다.

그리고 n이 1일때까지 연산을 하는 것이므로
n이 0or1일 경우 값은 0이기 때문에 2번째 값부터 구해주면 된다.

 */
void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int num;
    cin>>num;
    deque<int> dp(num);
    for(int i=2;i<num+1;++i){
        dp[i] = dp[i-1] + 1;
        if(i%5==0)
            dp[i] = min(dp[i],dp[i/5] + 1);
        if(i%3==0)
            dp[i] = min(dp[i],dp[i/3] + 1);
        if(i%2==0)
            dp[i] = min(dp[i],dp[i/2] + 1);
    }
    
    printArray(dp);
    
    cout<<dp[num]<<"\n";
}

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}