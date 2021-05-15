#include <bits/stdc++.h>
using namespace std;

// 계단오르기 
// https://www.acmicpc.net/problem/1535
void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,status = 100;
    cin>>N;
    deque<int> dp[N+1],GET(N+1),Loss(N+1);
    for(int i=1;i<=N;++i){
        cin>>Loss[i]>>GET[i];
    }
    // dp[n] = max(dp[n-2],dp[n-3]+temp[n-1]) + temp[n]
    // dp[4][2] = dp[3][1] + temp[4] = 1,3,4 or dp[4][1] = dp[2][1] + temp[4] = 1,2,4
    // dp[5][1] = dp[4][1] + temp[5] = 1,2,4,5 or dp[5][2] = dp[3][1] + temp[5] = 1,3,5
    // dp[6][1] = dp[5][1] + temp[6] = 1,2,4,6 or dp[6][2] = dp[5][2] + temp[6] =  1,3,5,6
    // or dp[6][3] = dp[4][2] + temp[6] = 1,3,4,6 
    for(int i=1;i<=N;++i){
        for(int j=100;j<=Loss[i];){
            if(j-Loss[i] >= 0){
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-Loss[i]]+GET[i]);
            }
            else{
                break;
            }
        }
    }
    printf("%d",dp[N][]);
    
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}