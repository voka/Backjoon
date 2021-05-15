#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int temp[10][10] ={0,}; // 종이판
int color_paper[5] = {5,5,5,5,5}; // 붙일 수 있는 색종이 5장
int N = 10;// NXN
int answer=25; // 아무리 많이 붙여도 25장 밖에 붙일 수 없다.


void update(int x, int y, int size,bool contents){
    for(int i = 0;i<size;++i){
        for(int j = 0;j<size;++j){
            temp[i+x][j+y] = contents;
        }
    }
}

bool check(int x,int y,int size){
    for(int i = 0;i<size;++i){
        for(int j = 0;j<size;++j){
            if(!temp[i+x][j+y]) return false;
        }
    }
    return true;
}
bool check2(){
    for(int i = 0;i<N;++i){
        for(int j = 0;j<N;++j){
            if(temp[i][j]) return false;
        }
    }
    return true;
}
void DFS_paper(int x, int y, int count){
    if(check2()){ // 종이에 1인 곳이 있는지 검사
        answer = min(answer,count); // 없으면 색종이가 다 덮였으므로 현재값과 새로구한 값 중 작은값을 정답으로
        return;
    }
    bool checks = false;
    for(x=0;x<N;++x){ // 종이판이 1인곳을 찾는다.
        for(y=0;y<N;++y){
            if(temp[x][y]){
                checks = true;
                break;
            }
        }
        if(checks){
            break;
        }
    }
    if(count>=answer)// 현재까지 구한 답이 최근에 구한 답보다 크면 미리 branch를 한다.
        return;

    for(int size=5;size>0;--size){// 5,4,3,2,1의 사이즈 순서로 차례로 색종이를 붙인다.
        if(x+size>N||y+size>N||color_paper[size-1] == 0) continue; // 색종이를 붙일 수 없거나, 붙일 색종이가 없는경우 제외한다.
        if(check(x,y,size)){ // x,y 부터 시작해 크기가 size인 색종이를 붙일 수 있는지 검사 
            update(x,y,size,0); // size X size만큼을 0으로 바꾼다
            --color_paper[size-1];//color color_paper 개수 감소
            DFS_paper(x,y,count+1);
            update(x,y,size,1);// 원상복구
            ++color_paper[size-1];// 원상복구
        }
    }
}

int main(void){
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            cin>>temp[i][j];
        }
    }
    DFS_paper(0,0,0);
    if(answer != 25) cout<<answer<<"\n";
    else cout<<-1<<"\n";
    return 0;
}