#include <bits/stdc++.h>
using namespace std;

// 앱
// https://www.acmicpc.net/problem/7579
/* void printArray(int a[],int N){
    for(int i=1;i<N;++i){
        cout<<a[i]<<",";
    }
    cout<<"\n";
} */
void solve(){ //1차원 배열
    int N,M,A[101],c[101],total_cost=0; // 앱의 수 N,  얻어야하는 메모리 M, 각 앱이 사용하는 메모리양 A, 각 앱을 비활성화 했을 경우의 비용 c 

    cin>>N>>M; 

    int dp[10001]={0,}; // 비용 만큼 배열이 존재해야 한다.
    for(int i=1;i<=N;++i){
        cin>>A[i];
    }
    for(int i=1;i<=N;++i){
        cin>>c[i];
        total_cost += c[i];
    }
    for(int i=1;i<=N;++i){
        for(int j=total_cost;j>=c[i];--j){
            dp[j] = max(dp[j],dp[j-c[i]]+A[i]);//현재 cost에서 확보할 수 있는 최대 메모리
        }
    }
    for(int i=1;i<=total_cost;++i){
        if(dp[i]>=M){
            printf("%d\n",i);
            break;
        }
    }
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}