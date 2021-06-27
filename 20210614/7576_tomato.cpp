#include<bits/stdc++.h>
#define Loop(i,n) for(int i=1;i<=n;++i)
using namespace std;

int M,N;
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
int parm[1002][1002] = {0,};
bool check[1002][1002];
int i_x[1002] = {0,};
int i_y[1002] = {0,};
void bfs(int x,int y){
    Loop(i,4){
        int N_x = x + dx[i];
        int N_y = y + dy[i];
        if(N_x < 1 || N_x > M || N_y < 1 || N_y > N) continue;
        if(parm[N_x][N_y] + 1 == 0 || check[N_x][N_y]) continue;
        if(parm[N_x][N_y] == 0) parm[N_x][N_y]++;
        check[N_x][N_y] = true;
    }
}
bool chk(){
    Loop(i,N){
        Loop(j,M){
            cin>>parm[i][j];
            if(parm[i][j] == 0) return false;
        }
    }
    return true;
}

int main(void){
    int num = 0;
    cin>>M>>N;
    Loop(i,N){
        Loop(j,M){
            cin>>parm[i][j];
            if(parm[i][j] == 1){
                i_x[num] = i;
                i_y[num] = j;
                num++;
            }
        }
    }
    int depth = 0;
    while(1){
        if(chk()) break;
        Loop(i,num){
            if(parm[i_x[i]][i_y[i]] + 1 != 0 && !check[i_x[i]][i_y[i]]) bfs(i_x[i],i_y[i]);
        }
        depth++;
        cout<<depth<<"\n";
    }
}