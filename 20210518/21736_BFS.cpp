#include<iostream>
#define Loop(i,s,e) for(int i=s;i<e;++i)
using namespace std;

int temp[601][601] = {0,}; // 1 : X, 2: P, 3 : O (빈공간)
int N,M,answer = 0;
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
int check[601][601] = {0,};
void BFS(int x, int y){
    Loop(i,0,4){
        int new_x = dx[i] + x;
        int new_y = dy[i] + y;
        if(check[new_x][new_y] == 1) continue;
        if(new_x >= N || new_x < 0 || new_y < 0 || new_y >= M) continue;
        if(temp[new_x][new_y] == 1 ) continue;
        if(temp[new_x][new_y] == 2 ) answer++;  
        check[new_x][new_y] = 1;
        BFS(new_x,new_y);
    }
}

int main(void){
    cin>>N>>M;
    int a,b;
    Loop(i,0,N){
        Loop(j,0,M){
            char k;
            cin>>k;
            int target = 0;
            if(k == 'O') target = 3;
            else if(k == 'P') target = 2;
            else if(k == 'X') target = 1;
            else {
               a = i;
               b = j; 
            }
            temp[i][j] = target;
        }
    }
    BFS(a,b);
    if(answer == 0)
        cout<<"TT"<<"\n";
    else
        cout<<answer<<"\n";
}
