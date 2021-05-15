#include <bits/stdc++.h>
using namespace std;

// 동전1
// https://www.acmicpc.net/problem/2293

void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,num;
    cin>>N>>num;
    deque<int> dp(num+1,0),money;
    for(int i=0;i<N;++i){
        int temp;
        cin>>temp;
        money[i] = temp;
    }
    dp[0] = 1;
    for(int j=0;j<N;++j){
        for(int i=1;i<=num;++i){
            if(money[j] <= i) dp[i] += dp[i-money[j]];
        }
        //printArray(dp);
    }
    cout<<dp[num];
    
}

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}