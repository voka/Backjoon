#include<bits/stdc++.h>
#define Loop(i,n) for(int i=1;i<=n;++i)
#define vLoop(i,a) for(auto i : a)
using namespace std;

int N,M;
int miro[1002][1002] = {0,};
int dx[5] = {0,0,0,1,-1};
int dy[5] = {0,1,-1,0,0};
int check[1001][1001][2] = {0,};
struct Point
{
    int x;
    int y;
    int bw;
    /* data */
};


int BFS(){
    queue<Point> Q;
    check[1][1][0] = 1;
    Q.push({1,1,0});
    while(!Q.empty()){
        Point cur = Q.front();
        Q.pop();
        int x = cur.x;
        int y = cur.y;
        if(x == M && y == N) return check[y][x][cur.bw];
        Loop(i,4){
            Point next;
            int new_x = x + dx[i];
            int new_y = y + dy[i];
            next.x = new_x;
            next.y = new_y;
            next.bw = cur.bw;
            if(new_x < 1 || new_y < 1 || new_x > M || new_y >N) continue;
            if(check[new_y][new_x][cur.bw] != 0) continue;
            if(miro[new_y][new_x] == 0){
                check[new_y][new_x][next.bw] = check[y][x][cur.bw] + 1;
                Q.push({new_x,new_y,cur.bw});
            }
            if(miro[new_y][new_x] == 1 && next.bw == 0){
                check[new_y][new_x][1] = check[y][x][cur.bw] + 1;
                next.bw = 1;
                Q.push(next);
            }
        }   

    }
    return -1;
    //cout<<y<<", "<<x<<", dp = "<<dp[y][x]<<"\n";
    
}

int main(void){
    cin>>N>>M;
    Loop(i,N){
        string s;
        cin>>s;
        int j = 1;
        vLoop(a,s){
            miro[i][j++] = a - '0';
        }
    }
    cout<<BFS();
    return 0;
}