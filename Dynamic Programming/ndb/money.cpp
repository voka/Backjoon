#include <bits/stdc++.h>
using namespace std;
/* 
Q. 효율적인 화폐구성

- 문제 설명

N가지 종류의 화폐 중에서 화폐의 개수를 최소한으로 이용해 그 가치의 합이 M원이 되도록 한다. 화폐 갯수는 무제한이며 순서가 달라도 같은 걸로 친다.
불가능시 -1을 출력한다.

 */
void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,num;
    cin>>N>>num;
    deque<int> dp(num+1,10001),money;
    for(int i=0;i<N;++i){
        int temp;
        cin>>temp;
        money[i] = temp;
    }
    dp[0] = 0;
    for(int j=0;j<N;++j){
        //cout<<"money : "<<money[j]<<"\n";
        for(int i=money[j];i<=num;++i){
            dp[money[j]] = 1;
            if(dp[i-money[j]]!= 10001) {
                dp[i] = min(dp[i],dp[i-money[j]] + 1);
            }
        }
        //printArray(dp);
    }
    if(dp[num]!=10001){
        cout<<dp[num];
    }
    else{
        cout<<-1;
    }
}

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}