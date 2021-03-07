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
    deque<int> dp(N);
    for(int i=1,j=0;i<=N;++i){
        cin>>t;
        if(i==1){
            dp[j++] = t;
        }
        else{
            if(dp[j]<t){
                dp[j++] = t;
            }
        }
    }
    printArray(dp);
    
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}