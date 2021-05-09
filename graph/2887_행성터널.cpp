#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
//간선 정보를 담는 클래스
struct Point{
    int x;
    int y;
    int z;
};

bool cmp(Point a, Point b){
    if(a.x != b.x){
        if(a.y != b.y){
            return a.z<b.z;
        }
        return a.y<b.y;
    }
    return a.x<b.x;
}

class Edge{
public://누구나 접근 가능
    Point node[2];
    int distance;
    //생성자 선언
    Edge(Point a, Point b, int distance){
        this->node[0] = a;
        this->node[1] = b;
        this->distance = distance;
    }
    bool operator <(Edge &edge){//연산자 오버로딩 -> 나중에 공부할 것 !
        return this -> distance < edge.distance;
    }
};
vector<Point> temp;
vector<Edge> planet;
int getParent(int parent[], int x){
    if(parent[x] == x) return x;
    return parent[x] = getParent(parent,parent[x]);
}

void unionParent(int parent[], int a, int b){
    a = getParent(parent,a);
    b = getParent(parent,b);
    if(a<b) parent[b] = a;
    else parent[a] = b;
}

int findParent(int parent[],int a,int b){
    a = getParent(parent,a);
    b = getParent(parent,b);
    if(a == b) return 1;
    else return 0;
}

int main(void){
    int n,a,b,c;
    cin>>n;
    for(int i=0;i<n;++i){
        cin>>a>>b>>c;
        temp.push_back(Point{a,b,c});
    }
    
    //간선의 비용을 기준으로 오름차순 정렬
    sort(temp.begin(),temp.end(),cmp);
    int answer = 0;
    for(auto i = temp.begin();i<temp.end()-1;++i){
        auto j = i + 1;
        printf("answer = %d , x = %d, y = %d, z = %d\n\n",answer,(*i).x,(*i).y,(*i).z);
        answer += min(abs((*i).x - (*j).x),min(abs((*i).y-(*j).y),abs( (*i).z-(*j).z ) ) );
    }
    printf("%d",answer);
    /* //그래프 저장
    int parent[n];
    //노드는 1번부터 시작 
    for(int i=1;i<n;++i){
        parent[i]=i;
    }
    int sum = 0;
    //사이클이 발생하지 않는경우 그래프에 포함시키기
    for(int i=0;i<v.size();++i){
        if(!findParent(parent,v[i].node[0],v[i].node[1])){
            sum += v[i].distance;
            unionParent(parent,v[i].node[0],v[i].node[1]);
        }
    }
    printf("최솟값은 %d입니다.\n",sum); */
}