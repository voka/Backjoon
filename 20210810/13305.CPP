#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;
void solve(){
    int N;
    cin>>N;
    vector<int> road(N-1),id(N);
    vector<long long> price(N);
    long long answer = 0;
    for(int i=0;i<N-1;++i){
        cin>>road[i];
    }
    for(int i=0;i<N-1;++i){
        cin>>price[i];
    }
    
    int pre = 0;
    id[pre] = road[0];
    for(int i=1;i<N-1;++i){
        if(price[i]>= price[pre]){
            id[pre] += road[i];
        }
        else{
            answer += price[pre] * id[pre];
            pre = i;
            id[pre] += road[i];
        }
    }
    answer += price[pre] * id[pre];
    cout<<answer<<"\n";

}

int main(void){
    solve();
    return 0;
}