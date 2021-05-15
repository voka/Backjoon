#include <bits/stdc++.h>
using namespace std;

// 계단오르기 
// https://www.acmicpc.net/problem/2579
// 아놔 deque는 처음에 크기 선언 안해줘도 되는 줄 알았는데 안해주니까 자꾸
// Out of index에러 떠서 고쳐줬는데 됐다. 다음부턴 무조건 크기 선언 해줍시다.. ㅎ
void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,num;

    cin>>N;
    int t;
    deque<int> dp(N+1),temp(N+1);
    temp[0] = 0;
    for(int i=1;i<=N;++i){
        cin>>t;
        temp[i] = t;
    }
    dp[0] = 0;
    dp[1] = temp[1]; 
    dp[2] = temp[1] + temp[2];// dp[2][1] = 1,2
    // dp[n] = max(dp[n-2],dp[n-3]+temp[n-1]) + temp[n]
    // dp[4][2] = dp[3][1] + temp[4] = 1,3,4 or dp[4][1] = dp[2][1] + temp[4] = 1,2,4
    // dp[5][1] = dp[4][1] + temp[5] = 1,2,4,5 or dp[5][2] = dp[3][1] + temp[5] = 1,3,5
    // dp[6][1] = dp[5][1] + temp[6] = 1,2,4,6 or dp[6][2] = dp[5][2] + temp[6] =  1,3,5,6
    // or dp[6][3] = dp[4][2] + temp[6] = 1,3,4,6 
    for(int i=3;i<=N;++i){
        dp[i] = max(dp[i-2],dp[i-3]+temp[i-1]) + temp[i];
    }
    printf("%d",dp[N]);
    
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}