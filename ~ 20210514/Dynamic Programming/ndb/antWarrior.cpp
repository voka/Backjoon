#include <bits/stdc++.h>
using namespace std;
/* 
개미전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다. 
메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있다.
각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다. 
이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다. 
따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다. 

예를 들어 식량창고 4개가 다음과 같이 존재한다고 가정하자
이때 개미 전사는 두 번째 식량창고와 네 번째 식량창고를 선택했을 때 최댓값인 총 8개의 식량을 빼앗을 수 있다.
개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 원한다.

개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 식량창고의 개수 N이 주어진다. (3<=N<=100)
둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. (0<=K<=1,000)

예시1.
input :
    1 3 1 5
output : 
    3+5 = 8

예시2.
input :
    1 3 1 5 7
output : 
    3+7 = 10

풀이방법

bottom -> up 방식으로 풀어보겠습니다.
dp[n]을 n번 까지의 식량창고를 약탈했을 때 얻을 수 있는 식량의 최대 값이라고 생각해 봅시다.
그러면, 
dp[0] = temp[0]
dp[1] = max(temp[0],temp[1])
dp[2] = max(dp[0] + temp[2],dp[1])가 될 것입니다.
(1,3번째 식량창고의 식량 수를 더한값과 2번째 식량창고의 식량 수 중 큰 값)
그리고 dp[3]은 max(dp[1] + temp[3],dp[2])가 될 겂입니다.
이런식으로 하다보면 점화식을 세울 수 있습니다.
dp[n] = max(dp[n-2]+temp[n],dp[n-1])
 */

void printArray(deque<int> a){
    for(auto i : a){
        cout<<i<<", ";
    }
    cout<<"\n";
}
void solve(){
    int N,temp_num;
    cin>>N;
    deque<int> dp,temp;
    for(int i=0;i<N;++i){
        cin>>temp_num;
        temp.push_back(temp_num);
    }
    dp[0] = temp[0];
    dp[1] = max(temp[0],temp[1]);
    for(int i=2;i<N;++i){
        dp[i] = max(temp[i] + dp[i-2],dp[i-1]);
    }
    printArray(dp);
    cout<<dp[N-1];
}

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}