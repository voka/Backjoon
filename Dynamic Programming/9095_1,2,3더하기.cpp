#include <bits/stdc++.h>
using namespace std;
// 1,2,3 더하기
// https://www.acmicpc.net/problem/9095

void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,num;

    cin>>N;
    int temp[N+1],t,answer[N+1];
    for(int i=0;i<N;++i){
        cin>>t;
        temp[i] = t;
        answer[i] = t;
    }
    sort(temp,temp+N);
    deque<int> dp;
    num = temp[N-1];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i=4;i<=num;++i){
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
    }
    for(int i=0;i<N;++i){
        printf("%d\n",dp[answer[i]]);
    }
    
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}