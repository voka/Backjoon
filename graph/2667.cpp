#include <bits/stdc++.h>
#define Loop(i,s,n) for(int i=s;i<n;++i) 
using namespace std;
class location{//위치 class;
public:
    location(int x,int y) : x(x), y(y){ }
    int x;
    int y;
};
template <typename Type>
void printdeque(deque<deque<Type>> check){// 출력
    Loop(i,0,check.size()){
        Loop(j,0,check[0].size()){
            cout<<check[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}
stack<location> reg;
template <typename T1,typename T2>
void execute(deque<deque<T1>> &check, deque<deque<T2>> &maps, int i, int j,int* r){
    if(check[i][j] == true){//자기 자신이 true
        check[i][j] = false;
        maps[i][j] += 1;
        //차례로 상하좌우 검사
        if(check[i-1][j] == true)//위쪽 true
            reg.push(location(i-1,j));
        if(check[i+1][j] == true)//밑쪽 true
            reg.push(location(i+1,j));
        if(check[i][j-1] == true)//왼쪽 true
            reg.push(location(i,j-1));
        if(check[i][j+1] == true)//오른쪽 true
            reg.push(location(i,j+1));
        *r = *r + 1;
        while(!reg.empty()){
            i = reg.top().x;
            j = reg.top().y;
            reg.pop();
            execute(check,maps,i,j,r);
        }
    }
}
int main(void){
    int N,t=0;
    char temp;
    cin>>N;
    deque<location> mem;
    deque<int> store;
    //인덱스 접근이 편하도록 바깥에 0으로 테두리 만듬
    deque<deque<int>> maps(N+2,deque<int>(N+2));//printdeque(maps)로 보여주기 용
    deque<deque<bool>> check(N+2,deque<bool>(N+2));//실제 필요한 deque
    Loop(i,1,N+1){
        Loop(j,1,N+1){
            cin>>temp;
            if(temp == '1'){
                check[i][j] = true;
                mem.push_back(location(i,j));
            }
            else
                check[i][j] = false;
        }
    }
    Loop(j,0,mem.size()){
        if(check[mem[j].x][mem[j].y]==true){
            execute(check,maps,mem[j].x,mem[j].y,&t);
            store.push_back(t);
            t = 0;
        }
    }
    cout<<store.size()<<"\n";;
    sort(store.begin(),store.end());
    Loop(i,0,store.size()){
        cout<<store[i]<<"\n";
    }
    return 0;
}
