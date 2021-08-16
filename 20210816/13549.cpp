#include <iostream>
#include <vector>
#include <queue>
#define pii pair<int,int>
using namespace std;
int INF = 1000000000;
int N,K;
vector<int> d(100001);

void find_boy(){
    queue<pii> q;
    d[N] = 0;
    q.push({N,0});
    int cur_boy = K;
    int t = 0;
    while(!q.empty()){
        int cur_my = q.front().first;
        int cur_t = q.front().second;
        q.pop();
        if(2*cur_my <= 100000){
            if(d[2*cur_my] > cur_t) {
                d[2*cur_my] = cur_t;
                q.push({2*cur_my,cur_t});
            }
        }
        if(cur_my + 1 <= 100000){
            if(d[cur_my+1] > cur_t + 1) {
                d[cur_my+1] = cur_t+1;
                q.push({cur_my+1,cur_t+1});
            }
        }
        if(cur_my > 0){
            if(d[cur_my-1] > cur_t + 1){  
                d[cur_my-1] = cur_t+1;
                q.push({cur_my-1,cur_t+1});
            }
        }
        
    }
}
void solve(){
    for(int i=0;i<=max(N,K)+1;++i){
        d[i] = INF;
    }
    find_boy();
    cout<<d[K]<<"\n";

}

int main(void){
    cin>>N>>K;
    solve();
    return 0;
}