#include <bits/stdc++.h>
using namespace std;

// 제곱수의 합
// https://www.acmicpc.net/problem/1699

void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N;
    cin>>N;
    deque<int> dp(100001);
    for(int i=1;i<=N;++i){
        dp[i] = i;
    }
    for(int j=2;j<=N;++j){
        for(int i=2;i*i<=j;++i){
            dp[j] = min(dp[j],dp[j - i*i]+1);
        }
    }
    cout<<dp[N]<<"\n";
    
}

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}