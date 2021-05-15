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
    for(int i=1,j=1;i<=N;++i){
        cin>>t;
        temp[i] = t;
    }
    dp[1] = temp[1];

    //printArray(dp);
    printf("%d",dp[N]);
    
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}