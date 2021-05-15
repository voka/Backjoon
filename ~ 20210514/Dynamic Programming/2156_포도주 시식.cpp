#include <bits/stdc++.h>
using namespace std;

// 포도주 시식
// https://www.acmicpc.net/problem/2156
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
    dp[2] = temp[1] + temp[2];
    dp[3] = max(dp[2],max(dp[1],temp[2])+temp[3]);
    for(int i=4;i<=N;++i){
        dp[i] = max(dp[i-1],max(dp[i-2],dp[i-3]+temp[i-1]) + temp[i]);
    }
    //printArray(dp);
    printf("%d",dp[N]);
    
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}