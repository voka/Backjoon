#include<iostream>
#include<algorithm>
#include <cstring>
#define Loop(i,s,n) for(int i=s;i<n;++i)

using namespace std;
struct Point{
    int x;
    int y;
};

Point temp[25001]={0,};
int K,N,M,answer = 0;
int bachu_bat[52][52] = {0,};
int check[52][52] = {0,};
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

void Find_bachu(int x, int y, int num){
    int flag = 0;
    Loop(i,0,4){
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        if(new_x < 0 || new_x > M || new_y <0 || new_y > N) continue;
        if(check[new_y][new_x] == 1 || bachu_bat[new_y][new_x] == 0) continue;
        check[new_y][new_x] = 1;
        Find_bachu(new_x,new_y,num+1);
    }
}
int main(void){
    int T;
    cin>>T;
    while(T--){
        cin>>M>>N>>K;
        answer = 0;
        Loop(i,0,K){
            int x,y;
            cin>>x>>y;
            bachu_bat[y][x] = 1;
            temp[i].x = x;
            temp[i].y = y;
        }
        Loop(i,0,K){
            int x=temp[i].x,y=temp[i].y;
            if(!check[y][x]){
                check[y][x] = 1;
                Find_bachu(x,y,1);
                answer++;
            }
        }
        memset(bachu_bat, 0, sizeof(bachu_bat));
        memset(check, 0, sizeof(check));
        cout<<answer<<"\n";
    }
    return 0;
}