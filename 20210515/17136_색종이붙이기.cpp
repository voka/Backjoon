#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int temp[10][10] ={0,};
int paper[5] = {5,5,5,5,5};
int N = 10;
int answer=123234123;


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
void find_paper(int x, int y, int count){
    if(check2()){
        answer = min(answer,count);
        return;
    }
    bool checks = false;
    for(x=0;x<N;++x){
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
    if(count>=answer)
        return;

    for(int size=5;size>0;--size){
        if(x+size>N||y+size>N||paper[size-1] == 0) continue;
        if(check(x,y,size)){
            update(x,y,size,0);
            --paper[size-1];
            find_paper(x,y,count+1);
            update(x,y,size,1);
            ++paper[size-1];
        }
    }
}

int main(void){
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            cin>>temp[i][j];
        }
    }
    find_paper(0,0,0);
    if(answer != 123234123) cout<<answer<<"\n";
    else cout<<-1<<"\n";
    return 0;
}