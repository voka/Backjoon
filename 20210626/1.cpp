#include<bits/stdc++.h>
#define Loop(i,n) for(int i=1;i<=n;++i)
#define vLoop(i,a) for(auto i : a)
using namespace std;

int N,M,MAX_INT = 100000001;
int miro[1002][1002] = {0,};
int dp[1002][1002] = {0,};
int dx[5] = {123,1,0,-1,0};
int dy[5] = {123,0,1,0,-1};
bool check[1001][1001];
void DFS(int x, int y,bool flag){
    //cout<<y<<", "<<x<<", dp = "<<dp[y][x]<<"\n";
    if(x == M && y == N) return;
    Loop(i,4){
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        if(new_x < 1 || new_y < 1 || new_x > M || new_y >N) continue;
        if(check[new_y][new_x]) continue;
        if(miro[new_y][new_x] == 1){
            if(!flag) flag = true;
            else continue;
        }
        if( dp[new_y][new_x] < dp[y][x] + 1) continue; 
        else dp[new_y][new_x] = dp[y][x] + 1;
        check[new_y][new_x] = true;
        DFS(new_x,new_y,flag);
        //flag = false;
        //check[new_y][new_x] = false;
    }
}

int main(void){
    cin>>N>>M;
    Loop(i,N){
        string s;
        cin>>s;
        int j = 1;
        vLoop(a,s){
            dp[i][j] = MAX_INT;
            miro[i][j++] = a - '0';
        }
    }
    dp[1][1] = 1;
    check[1][1] = true;
    DFS(1,1,false);
    if(dp[N][M] == MAX_INT) cout<<-1<<"\n";
    else cout<<dp[N][M]<<"\n";
    return 0;
}