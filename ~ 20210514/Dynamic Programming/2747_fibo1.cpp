#include <bits/stdc++.h>
using namespace std;

// 피보나치수 1
// https://www.acmicpc.net/problem/2747

deque<int> fibo(10001);

void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,num;

    cin>>N; 
    fibo[0] = 0;
    fibo[1] = 1;
    fibo[2] = 1;
    for(int i=3;i<=N;++i){
        fibo[i] = fibo[i-1] + fibo[i-2];
    }
    cout<<fibo[N]<<"\n";
    
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}