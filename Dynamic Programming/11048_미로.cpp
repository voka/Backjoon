#include <bits/stdc++.h>
using namespace std;

// 이동하기
// https://www.acmicpc.net/problem/11048

int miro[1001][1001] = {0,},dp[1001][1001]= {0,};
int N,M;

void printArray(int n, int m){
    for(int i=0; i<=n+1;++i){
        for(int j=0;j<=m+1;++j){
            cout<<dp[i][j]<<", ";
        }
        cout<<"\n";   
    }
}


void solve(){
    cin>>N>>M; 
    for(int i=1; i<=N;++i){
        for(int j=1;j<=M;++j){
            cin>>miro[i][j];
        }
    }
    
    for(int i=1; i<=N;++i){
        for(int j=1;j<=M;++j){
            dp[i][j] = max(max(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1]) + miro[i][j]; 
        }
    }
    //printArray(N,M);
    cout<<dp[N][M];
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}