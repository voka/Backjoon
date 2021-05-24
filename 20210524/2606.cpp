#include<iostream>
#include<algorithm>
#include<vector>
#define Loop(i,s,n) for(int i=s;i<n;++i)

using namespace std;

struct Node{
    vector<int> next;
};

Node computers[100];
int N,M,check[101]={0,},num=0;

void DFS(int x){
    int size = computers[x].next.size();
    Loop(i,0,size){
        int next = computers[x].next[i];
        if(!check[next]){
            //cout<<"x == "<<x << "next == "<<next<<"\n";
            check[next] = 1;
            num++;
            DFS(next);
        }
    }
}

int main(void){
    cin>>N>>M;
    Loop(i,0,M){
        int t,temp;
        cin>>t>>temp;
        computers[t].next.push_back(temp);
        computers[temp].next.push_back(t);
    }
    check[1] = 1;
    DFS(1);
    cout<<num<<"\n";
}
