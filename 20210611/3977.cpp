#include<bits/stdc++.h>
#define Loop(i,n) for(int i=1;i<=n;++i)
#define Loop2(a,v) for(auto a : v)
using namespace std;
struct Node{
    vector<int> next;
};
bool operator<(Node a, Node b){
    return a.next<b.next;
}
int V,E;
int check[100001];
int SCC[100002] = {0,};
int indegree[100002] = {0,};
vector<Node> bucket(100001);
vector<Node> rbucket(100001);
stack<int> temp;
void DFS(int x){
    check[x] = true;
    Loop2(i,bucket[x].next){
        if(check[i]) continue;
        DFS(i);
    }
    temp.push(x);
}

// 위상정렬
void DFS2(int x,int num){
    SCC[x] = num;
    Loop2(i,rbucket[x].next){
        if(SCC[i] == 0) DFS2(i,num); // 진입차수 0 재귀 
        else if(SCC[i] != SCC[x]){ // SCC 그룹이 다르면
            indegree[SCC[x]]++; // 증가 시킴.
            continue;
        }
    }
}

int main(void){
    int T;
    cin>>T;
    while(T--){
        int a_index=0;
        cin>>V>>E;
        Loop(i,E){
            int a,b;
            cin>>a>>b;
            bucket[a+1].next.push_back(b+1);
            rbucket[b+1].next.push_back(a+1);
        }
        Loop(i,V){
            if(!check[i]) DFS(i);
        }
        int SCC_num=1;
        while(!temp.empty()){
            int x = temp.top();
            temp.pop();
            if(SCC[x]) continue;
            DFS2(x,SCC_num);
            SCC_num++;
        }
        int answer=0;
        int answers_index = 0;
        Loop(i,SCC_num-1){
            if(indegree[i] == 0) {
                answer++; 
                answers_index  = i;
                if(answer != 1){
                    break;
                } 
            }
        }
        if(answer >= 2){
            cout<<"Confused\n\n";
        }
        else{
            Loop(i,V){
                if(SCC[i] == answers_index){
                    cout<<i-1<<"\n";
                }
            }
            cout<<"\n";
        }
        //init
        fill(check,check+V+1, 0);
        fill(SCC,SCC+V+1, 0);
        fill(indegree,indegree+V+1, 0);
        Loop(i,V){
            bucket[i].next.clear();
            rbucket[i].next.clear();
        }
    }

}