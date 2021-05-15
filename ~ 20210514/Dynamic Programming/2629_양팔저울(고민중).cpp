#include <bits/stdc++.h>
using namespace std;

// 양팔저울
// https://www.acmicpc.net/problem/2629




void solve(){
    int N,chu[31],M,target[31],sum=0;
    deque<int> dp(40001);
    cin>>N;
    for(int i=1;i<=N;++i){
        cin>>chu[i];
        dp[chu[i]] = chu[i];
        sum += chu[i];
        dp[sum] = sum;
    }
    cin>>M;
    for(int i=1;i<=M;++i){
        cin>>target[i];
    }
    for(int i=1;i<=sum;++i){
        for(int j=1;j<=N;++j){

        }
    }   
    for(int i=1;i<=M;++i){
        if(dp[target[i]]==1) cout<<"Y ";
        else cout<<"N ";
    } 
}
int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}