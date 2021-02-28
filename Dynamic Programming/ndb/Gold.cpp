#include <bits/stdc++.h>
using namespace std;
/* 
n × m 크기의 금광이 있다. 금광은 1 × 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의
금이 들어 있다
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라
 */

void solve(){
    int N,M;
    cin>>N>>M;
    int maps[M+1][N+1],dp[M+1][N+1];
    //데이터 입력받기 및 dp 배열 초기화
    for(int i=0;i<N;++i){
        for(int j=0;j<M;++j){
            cin>>maps[i][j];
            dp[i][j] = 0;
        }
    }
    //dp시작
    for(int i=0;i<M;++i){
        for(int j=0;j<N;++j){
            //첫 열 데이터 입력
            if(i == 0){
                dp[j][i] = maps[j][i];
            }
            else{
                // 맨 위쪽인 경우, 맨 아래쪽인 경우 그게 아닌 경우로 구분함.
                if(j==0) dp[j][i] = maps[j][i]+ max(dp[j][i-1],dp[j+1][i-1]);
                else if(j == N-1) dp[j][i] = maps[j][i]+ max(dp[j][i-1],dp[j-1][i-1]);
                else {
                    int temp = max(dp[j][i-1],dp[j-1][i-1]);
                    dp[j][i] = maps[j][i] + max(temp,dp[j+1][i-1]);
                }
            }
        }
    }
    int answer = 0;
    for(int i=0;i<N;++i){
        answer = max(answer,dp[i][M-1]);
    }
    cout<<answer<<"\n";
}

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int T = 0;
    cin>>T;
    for(int i=0;i<T;++i){
        solve();
    }
    return 0;
}

/*  동빈나 님의 코드 (python)
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)







 */