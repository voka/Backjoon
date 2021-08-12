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
    int s = my.size() - 1 ;
    vector<int> answer(s+1,-1),romor(s+1,0);
    queue<pair<int,int>> q;
    bool check[s+1] = {0,};
    for(auto i : starter){
        check[i] = true;
        answer[i] = 0;
        q.push({i,0});
    }
    while(!q.empty()){
        int cur = q.front().first;
        int next_t = q.front().second + 1; // 다음 시간
        //cout<<"cur == "<<cur<<", time == "<<next_t<<" my[cur].S == " << my[cur].S<<"\n";
        q.pop();
        for(auto l : my[cur].next){
            romor[l] += 1;
        }
        if(my[cur].S == 0) continue;
        for(auto k : my[cur].next){
            if(check[k]) continue;
            //cout<<"k == "<<k<<", my[k].suc == "<<my[k].suc<<", romor[k] == "<<romor[k]<<"\n";
            if(my[k].suc <= romor[k]){
                check[k] = true;
                answer[k] = next_t;
                q.push({k,next_t});
            }
        }
    }
    for(int i=1;i<=s;++i) cout<<answer[i]<<" ";
}

void solve(){
    int N,M;
    cin >> N;
    vector<Graph> my(N+1);
    for(int i=1;i<=N;++i){
        int a = -1;
        while(1){
            cin>>a;
            if(a == 0) break;
            my[i].next.push_back(a);
        }
        int t = my[i].next.size();
        my[i].S = t;
        if(t != 0) {
            if(t & 1){
                my[i].suc = 1 + t/2;
            }
            else my[i].suc = t/2;
            
        }
        else my[i].suc = 0;
    }
    cin>>M;
    vector<int> starter(M);
    for(int i=0;i<M;++i){
        cin>>starter[i];
    }
    BFS(my,starter);

}
int main(void){
    solve();
    return 0;
}