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
int V,E,a_index=0;
int check[10001];
int rcheck[10001];
vector<Node> bucket(10001);
vector<Node> rbucket(10001);
Node a;
vector<Node> answer;
stack<int> temp;
queue<int> last;
void DFS(int x){
    check[x] = true;
    Loop2(i,bucket[x].next){
        if(check[i]) continue;
        DFS(i);
    }
    temp.push(x);
}

void DFS2(int x){
    rcheck[x] = true;
    Loop2(i,rbucket[x].next){
        if(rcheck[i]) continue;
        DFS2(i);
    }
    a.next.push_back(x); 
}

int main(void){
    cin>>V>>E;
    Loop(i,E){
        int a,b;
        cin>>a>>b;
        bucket[a].next.push_back(b);
        rbucket[b].next.push_back(a);
    }
    Loop(i,V){
        if(!check[i]) DFS(i);
    }
    while(!temp.empty()){
        int x = temp.top();
        temp.pop();
        if(rcheck[x]) continue;
        DFS2(x);
        sort(a.next.begin(),a.next.end());
        answer.push_back(a);
        a.next.clear();
        a_index++;
    }
    sort(answer.begin(),answer.end());
    cout<<a_index<<"\n";
    Loop(i,a_index){
        Loop2(j,answer[i-1].next){
            cout<<j<<" ";
        }
        cout<<-1<<"\n";
    }
    cout<<"\n";
}