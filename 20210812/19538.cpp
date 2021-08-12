#include<iostream>
#include<vector>
#include<queue>
using namespace std;

struct Graph
{
    int S;//size
    int suc;
    vector<int> next;
};


void BFS(vector<Graph> & my, vector<int> & starter){
    int s = my.size() - 1 ; // N 
    vector<int> answer(s+1,-1),romor(s+1,0); // 정답, 자신의 이웃중 몇명이 소문을 믿고 있는지 저장할 벡터
    queue<pair<int,int>> q; // {방문지점, 시간}을 저장하면서 BFS를 진행할 queue 선언
    bool check[s+1] = {0,}; // 방문했는지 여부 점검
    for(auto i : starter){ // 시작하는 인원 모두 큐에 넣음.
        check[i] = true; // 방문표시
        answer[i] = 0; // 0분에 루머를 접했으므로 해당 시작점에 있는 사람들은 0분이 정답이됨.
        q.push({i,0}); // 큐에 삽입
    }
    while(!q.empty()){ // 큐가 비워졌을때
        int cur = q.front().first; // 방문지점
        int next_t = q.front().second + 1; // 다음 시간
        //cout<<"cur == "<<cur<<", time == "<<next_t<<" my[cur].S == " << my[cur].S<<"\n";
        q.pop();// pop
        for(auto l : my[cur].next){// 루머 접촉자 증가
            romor[l] += 1;
        }
        if(my[cur].S == 0) continue; // size == 0이면 for문 들어갈 필요도 없음.
        for(auto k : my[cur].next){
            if(check[k]) continue;// 방문했으면 cut
            //cout<<"k == "<<k<<", my[k].suc == "<<my[k].suc<<", romor[k] == "<<romor[k]<<"\n";
            if(my[k].suc <= romor[k]){ // 내 이웃 중 과반수가 rumor를 접했다면 나도 믿기 시작
                check[k] = true; // 방문 표시
                answer[k] = next_t; // next_n분에 소문을 믿게됨
                q.push({k,next_t});// 큐에 삽입
            }
        }
    }
    for(int i=1;i<=s;++i) cout<<answer[i]<<" "; // 정답 출력
}

void solve(){
    int N,M;
    cin >> N;
    vector<Graph> my(N+1); // 이웃 확인하는 그래프
    for(int i=1;i<=N;++i){
        int a = -1;
        while(1){
            cin>>a;
            if(a == 0) break; // 0이면 입력 종료
            my[i].next.push_back(a);
        }
        int t = my[i].next.size(); // 이웃 수 계산
        my[i].S = t; 
        if(t != 0) {  // 짝수 과반수, 홀수 과반수 계산.
            if(t & 1){
                my[i].suc = 1 + t/2;
            }
            else my[i].suc = t/2;
            
        }
        else my[i].suc = 0;
    }
    cin>>M;
    vector<int> starter(M); // 시작점 넣을 변수
    for(int i=0;i<M;++i){
        cin>>starter[i];
    }
    BFS(my,starter); // BFS 시작

}
int main(void){
    solve();
    return 0;
}