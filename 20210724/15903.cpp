#include<queue>
#include<iostream>
using namespace std;

void solve(){
    int N, act;
    long long int Answer = 0;
    cin>>N>>act;
    priority_queue<long long int,vector<long long int>,greater<long long int>> con;
    for(int i=0;i<N;++i){
        long long int x;
        cin>>x;
        con.push(x);
    }
    for(int i=0;i<act;++i){
        long long int a,b;
        a = con.top();
        con.pop();
        b = con.top();
        con.pop();
        con.push(a+b);
        con.push(a+b);
    }
    while(!con.empty()){
        Answer += con.top();
        con.pop();
    }
    cout<<Answer<<"\n";
}

int main(void){
    solve();
    return 0;
}