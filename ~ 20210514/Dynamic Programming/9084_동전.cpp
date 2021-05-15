#include <bits/stdc++.h>
using namespace std;

// 동전
// https://www.acmicpc.net/problem/9084

void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,M;
    cin>>N;
    deque<int> dp(10001),money(21);
    for(int i=0;i<N;++i){
        cin>>money[i];
    }
    cin>>M;
    dp[0] = 1;
    for(int j=0;j<N;++j){
        for(int i=money[j];i<=M;++i){
            dp[i] += dp[i-money[j]];
        }
    }
    cout<<dp[M]<<"\n";
    
}

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int T;
    cin>>T;
    for(int i=0;i<T;++i)
        solve();
    return 0;
}