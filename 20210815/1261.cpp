#include <iostream>
#include <vector>
#include <queue>
#define pii pair<int,int>
using namespace std;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int N,M;

vector<vector<int>> maps(101,vector<int>(101)); 
vector<vector<int>> dis(101,vector<int>(101)); 

int INF = 1000000000;



void dijkstra(){
    for(int i=1;i<=M;++i){
        for(int j=1;j<=N;++j){
            dis[i][j] = INF;//연결되지 않았을 때의 비용은 무한 
        }
    }
    dis[1][1] = 0;
    queue<pii> q;
    q.push({1,1});
    while(!q.empty()){
        pii cur = q.front();
        int x = cur.first;
        int y = cur.second;
        q.pop();
        for(int i=0;i<4;++i){
            int new_x = dx[i] + x;
            int new_y = dy[i] + y;
            if(new_x < 1 || new_x > M || new_y < 1 || new_y > N) continue;
            int n_dis =dis[x][y] + maps[new_x][new_y];
            if (dis[new_x][new_y] > n_dis)
            {
                dis[new_x][new_y] =  n_dis;
                q.push({new_x,new_y});
            }
        }
    }
    cout<<dis[M][N]<<"\n";
}
int main(void){
    cin>>N>>M;
    for(int i=1;i<=M;++i){
        string s;
        cin>>s;
        for(int a=1;a<=s.size();++a){
            maps[i][a] = s[a-1] - '0';
        }
    }
    
    dijkstra();
    
    
    return 0;
}
