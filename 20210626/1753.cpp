#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int V,E;
int INF = 1000000000;

vector<pair<int,int>> Graph[20001] ; //간선의 정보를 나타냄.
int d[20001]; // 최단거리 배열

void dijkstra(int start){
    d[start] = 0;
    priority_queue<pair<int,int>> q; // 기본적으로 가장 큰값이 위에 있는 구조 
                                    // 가장 작은 값이 맨 위로 오려면 음수화를 사용해야한다.
    q.push(make_pair(0,start));
    while(!q.empty()){
        int cur = q.top().second;
        int distance = -q.top().first;
        q.pop();
        if(d[cur]<distance) continue; // 최단거리가 아닌 경우 스킵
        for(int i=0;i<Graph[cur].size();++i){
            int next = Graph[cur][i].first; // 선택노드의 인접노드
            int nextdis = distance + Graph[cur][i].second; // 선택노드를 인접노드 거쳐서 가는 비용
            if(nextdis < d[next]){
                d[next] = nextdis;
                q.push(make_pair(-nextdis,next));
            }
        }
    }
}

int main(void){
    cin>>V>>E;
    int start;
    cin>>start;
    for(int i=1;i<=V;++i){
        d[i] = INF; //연결되지 않았을 때의 비용은 무한 
    }
    for(int i=1;i<=E;++i){
        int a,b,c;
        scanf("%d%d%d",&a,&b,&c);
        Graph[a].push_back(make_pair(b,c));
    }
    dijkstra(start);
    
    for(int i=1;i<=V;++i){
        if(d[i] != INF) printf("%d\n",d[i]);
        else printf("INF\n");
    }
    
    return 0;
}
