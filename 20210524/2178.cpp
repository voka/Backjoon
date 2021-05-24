#include<iostream>
#include<algorithm>
#include<string>
#include <cstring>
#define Loop(i,s,n) for(int i=s;i<n;++i)

using namespace std;
int K,N,M,answer = 10000;
int miro[101][101] = {0,};
int check[101][101] = {0,};
int dp[101][101] = {0,};
int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};

void find_miro(int x, int y, int num){
    if(x == M-1 && y == N-1){
        answer = min(answer,num);
        return;
    }
    Loop(i,0,4){
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        if(new_x < 0 || new_x >= M || new_y <0 || new_y >= N) continue;
        if(check[new_y][new_x] == 1 || miro[new_y][new_x] == 0) continue;
        if(dp[new_y][new_x] <= num+1) continue;
        dp[new_y][new_x] = num+1;
        check[new_y][new_x] = 1;
        find_miro(new_x,new_y,num+1);
        check[new_y][new_x] = 0;
    }
}
int main(void){
    cin>>N>>M;
    Loop(i,0,N){
        string s;
        cin>>s;
        Loop(j,0,s.size()){
            miro[i][j] = s[j] - '0';
        }
    }
    memset(dp, 10000, sizeof(dp));
    check[0][0] = 1;
    find_miro(0,0,1);
    cout<<answer<<'\n';
    return 0;
}