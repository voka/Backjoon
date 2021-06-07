#include<bits/stdc++.h>
#define Loop(i,n) for(int i=0;i<n;++i)
using namespace std;

int N,M,counts = 0;
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
int maps[501][501] = {0,};
int dp[501][501] = {0,};
int check[501][501] = {0,};
int DFS(int x,int y){
    if(x == N-1 && y == M-1){
        return 1;
    }
    if (dp[x][y] != -1)
		return dp[x][y];
    dp[x][y] = 0;
    Loop(i,4){
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        if(new_x < 0 || new_x >=N || new_y < 0 || new_y >= M) continue;
        if(maps[x][y] <= maps[new_x][new_y]) continue;
            dp[x][y] += DFS(new_x,new_y);
    }
    return dp[x][y];
}

int main(){
    cin>>N>>M;
    Loop(i,N){
        Loop(j,M){
            cin>>maps[i][j];
            dp[i][j] = -1;
        }
    }
    cout<<DFS(0,0)<<"\n";
}