#include<bits/stdc++.h>
#define Loop(i,n) for(int i=1;i<=n;++i)
#define Loop2(a,v) for(auto a : v)
using namespace std;
struct Node{
    vector<int> next;
};
int V,E,answer=0;
int SCC_num=1;
int check[500002] = {0,};
int dp[500002] = {0,};
int SCC[500002] = {0,};
int SCC_Group_sum[500002] = {0,};
vector<Node> bucket(500002);
vector<Node> rbucket(500002);
vector<Node> SCC_Group(500002);
stack<int> temp;
void DFS(int x){
    check[x] = true;
    Loop2(i,bucket[x].next){
        if(check[i]) continue;
        DFS(i);
    }
    temp.push(x);
}
void DFS2(int x,int num){
    SCC[x] = num;
    SCC_Group_sum[num]++;
    Loop2(i,rbucket[x].next){
        if(SCC[i] == 0) DFS2(i,num); // 진입차수 0 재귀 
        else if(SCC[i] != SCC[x]){ // SCC 그룹이 다르면
            SCC_Group[SCC[i]].next.push_back(SCC[x]); //요 벡터가 새로운 노드가 됌. -> 한 사이클당 큰 노드 1개로 변함.
        }
    }
}
int tcheck[1001] = {0,};
void DFS3(int x){
    tcheck[x] = true;
    

}
int main(void){
    cin>>V>>E;
    Loop(i,V){
        int a;
        cin>>a;
        bucket[a].next.push_back(i);
        rbucket[i].next.push_back(a);
    }
    Loop(i,V){// 모든 정점을 방문할 때 까지 DFS 1번
        if(!check[i]) DFS(i);
    }
    while(!temp.empty()){ // 반대방향으로 정점을 방문할 수 있다면 SCC가 된다.
        int x = temp.top();
        temp.pop();
        if(SCC[x]) continue;
        DFS2(x,SCC_num);
        SCC_num++;
    } 
    Loop(i,SCC_num-1){
        cout<<"i == "<<i<<":"<<SCC_Group_sum[i]<<"\n";
    }
    cout<<answer;
    cout<<"\n";
}