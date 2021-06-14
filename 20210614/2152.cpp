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
// 위상정렬
queue<int> tmp;
void TopologySort(int last){
	//모든 노드를 방문할 때 까지 반 복  
	while(!tmp.empty()){
		int j = tmp.front();
		tmp.pop();
        if(j == last){ // 끝점일때만 최대치 갱신
            answer = max(answer,dp[j]);
        }
        Loop2(a,SCC_Group[j].next){
            int w = SCC_Group_sum[a];
            if(dp[a] < dp[j] + w){
                dp[a] = dp[j] + w;
                tmp.push(a);
            }
        }
	}
}

int main(void){
    int start,last;
    cin>>V>>E>>start>>last;
    Loop(i,E){
        int a,b;
        cin>>a>>b;
        bucket[a].next.push_back(b);
        rbucket[b].next.push_back(a);
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
    int start_SCC = SCC[start];
    last = SCC[last]; 
    tmp.push(start_SCC);
    dp[start_SCC] = SCC_Group_sum[start_SCC];
    TopologySort(last);
    cout<<answer;
    cout<<"\n";
}