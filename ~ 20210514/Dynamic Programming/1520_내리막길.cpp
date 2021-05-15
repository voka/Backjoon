#include <bits/stdc++.h>
using namespace std;

// 내리막길
// https://www.acmicpc.net/problem/1520

int miro[501][501] = {0,},dp1[501][501]= {0,},dp2[501][501]= {0,};
bool check[501][501] = {false,};
int N,M;

void printArray(int n, int m){
    for(int i=0; i<=n+1;++i){
        for(int j=0;j<=m+1;++j){
            cout<<dp1[i][j]<<", ";
        }
        cout<<"\n";   
    }
}

void process(int s, int e){
    for(int i=s; i<=N;++i){
        for(int j=e;j<=M;++j){
            if((miro[i][j] - miro[i-1][j]<0) && dp1[i-1][j] >= 1)
                dp1[i][j] = dp1[i][j-1] + dp1[i-1][j];
            if((miro[i][j] - miro[i][j-1]<0) && dp1[i][j-1] >= 1)
                dp1[i][j] = dp1[i][j-1] + dp1[i-1][j];
        }
    }
}

void solve(){
    cin>>N>>M; 
    for(int i=1; i<=N;++i){
        for(int j=1;j<=M;++j){
            cin>>miro[i][j];
        }
    }
    dp1[1][1] = 1;
    
    process(1,1);
    printArray(N,M);
    
    for(int i=1; i<=N;++i){
        for(int j=1;j<=M;++j){
            if((miro[i][j] - miro[i+1][j]<0) && dp1[i+1][j] >= 1){
                dp2[i][j] += dp1[i+1][j];
                if(dp2[i][j] != 0) process(i,j);
            }
            if((miro[i][j] - miro[i][j+1]<0) && dp1[i][j+1] >= 1)
                dp2[i][j] += dp1[i][j+1];
                if(dp2[i][j] != 0)  process(i,j);
        }
    }
    printArray(N,M);

    cout<<dp1[N][M];
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}