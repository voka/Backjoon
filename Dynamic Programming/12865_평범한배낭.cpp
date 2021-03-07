#include <bits/stdc++.h>
using namespace std;

// 평범한 배낭
// https://www.acmicpc.net/problem/12865


/* 
    2차원 배열과 1차원 배열 두가지 방법으로 해결할 수 있으며, 
    1차원 배열을 쓰면 2차원 배열보다 시간이 반 이상 줄어든다.
    1차원 배열의 원리는 DP문제 중 동전 문제와 많이 유사하다.
    동전문제도 5원,10원,20원,50원 이런식으로 계속해서 동전을 사용했을때
    기존 사용했던 동전의 수 보다 작은 동전의 수로 대체할 수 있으면 그 값을 바꾸는 방법이었다.
    1차원 배열을 사용하는 것도 같은 방식으로 
    // w <- 무게 배열, v <- 가치 배열, N : 물건의 총 수, K : 무게값
    1. 물건의 무게 범위 만큼의 배열을 선언한다.
    2. 물건의 무게가 허용가능한 무게(K) 보다 작은지 확인한다.
    3. DP[K]와 DP[K-w[i]]+v[i]을 비교해 큰 값을 DP[K]에 넣는다.
    4. 2~3과정을 i : 1~N, j : K ~ 1까지 계속 반복한다.ㄴ
 */
void printArray(deque<int> a){
    for(auto i = a.begin();i!=a.end();++i){
        cout<<*i<<", ";
    }
    cout<<"\n";
}
/* void solve(){ //이중배열 version
    int N,K,w[101],v[101]; // 물품의 수 N,  버틸수 있는 무게 K, 각 물건의 무게 배열 w, 각 물건의 가치 배열 v 

    cin>>N>>K; 

    int dp[N+1][100001];
    for(int i=1;i<=N;++i){
        cin>>w[i]>>v[i];
    }
    for(int i=1;i<=N;++i){
        for(int j=1;j<=K;++j){
            if(j-w[i] >= 0)
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);
            else    dp[i][j] = dp[i-1][j];
        }
    }
    cout<<dp[N][K];
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
} */

void solve(){ //1차원 배열
    int N,K,w[101],v[101]; // 물품의 수 N,  버틸수 있는 무게 K, 각 물건의 무게 배열 w, 각 물건의 가치 배열 v 

    cin>>N>>K; 

    int dp[100001]={0,}; // 물건의 무게만큼 배열이 존재해야 한다.
    for(int i=1;i<=N;++i){
        cin>>w[i]>>v[i];
    }
    for(int i=1;i<=N;++i){
        for(int j=K;j>=1;--j){
            if(w[i] <= j) //넣을려고 하는 물건의 무게가 j 보다 작다면,
                dp[j] = max(dp[j],dp[j-w[i]]+v[i]);
        }
    }
    cout<<dp[K];
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}