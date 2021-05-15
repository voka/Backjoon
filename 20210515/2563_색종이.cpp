#include<iostream>
#include<algorithm>
using namespace std;
int board[100][100] = {0,};
int N;

int main(void){
    cin>>N;
    int max_x=0,max_y=0;
    for(int i=0;i<N;++i){
        int x,y;
        cin>>x>>y;
        max_x = max(max_x,x+10);
        max_y = max(max_y,y+10);
        for(int n=y;n<y+10;++n){
            for(int m=x;m<x+10;++m){
                if(board[n][m]) continue;
                board[n][m] = 1;
            }
        }
    }
    int answer = 0;
    for(int i=0;i<=max_y;++i){
        for(int j=0;j<=max_x;++j){
            if(board[i][j]) answer++;
        }
    }
    cout<<answer<<"\n";
}