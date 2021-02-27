#include <bits/stdc++.h>
using namespace std;

// 쉬운 계단 수
// https://www.acmicpc.net/problem/10844


/* 
dp[N][j] = dp[N - 1][j - 1] + dp[N - 1][j + 1]
 길이가 N 일 때, 마지막 수가 j일 경우의 계단 수

위 점화식은 j가 1~8사이일 때 성립한다.
0은 +1, 9는 -1만 적용되기 때문이다.

j =    0    => dp[N][j] = dp[N - 1][j + 1]
j = (1 ~ 8) => dp[N][j] = dp[N - 1][j - 1] + dp[N - 1][j + 1]
j =    9    => dp[N][j] = dp[N - 1][j - 1]


 */\
void solve(){
    int N,num;
    int MAX = 1000000000;
    cin>>N;
    int t;
    long dp[101][11] = {0,};
    for (int i = 1; i <= 9; i++) {
        dp[1][i] = 1;
    }
 
    for (int i = 2; i <= N; i++) {
        dp[i][0] = dp[i - 1][1];
        for (int j = 1; j <= 9; j++) {
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MAX;
        }
    }
    long sum = 0;
    for (int i = 0; i < 10; i++) {
        sum = (sum + dp[N][i])%MAX;
    }
    printf("%d",sum);
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}