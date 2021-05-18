#include<iostream>
#include<algorithm>
using namespace std;

int dp[1001][2][32] = {0,};
int N,W;
int jadu[1001] = {0,};
int max_num = 0;
void catch_jadu(){
    for(int i=1;i<=N;++i){
        for(int j=1;j<=W+1;++j){
            if(jadu[i] == 1){ // 1번 나무에서 잡을 떄 .
                dp[i][0][j] = max(dp[i-1][0][j] , dp[i-1][1][j-1] ) +1; 
                dp[i][1][j] = max(dp[i-1][0][j-1] , dp[i-1][1][j] );
            }
            else{
                if (i == 1 && j == 1) {
                    continue;
                }
                dp[i][0][j] = max(dp[i-1][0][j] , dp[i-1][1][j-1] );
                dp[i][1][j] = max(dp[i-1][0][j-1] , dp[i-1][1][j] ) +1;
            }
        }
    }
}

int main(void){
    cin>>N>>W;
    for(int i=0;i<N;++i){
        cin>>jadu[i];
    }
    catch_jadu();

    for(int j=1;j<=W;++j){
        max_num = max(max_num,max(dp[N][1][j],dp[N][0][j]));
    }
    cout<<max_num<<"\n";
}