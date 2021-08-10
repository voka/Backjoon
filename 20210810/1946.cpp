#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

struct ranks{
    int f;
    int s;
};
bool cmp(ranks a,ranks b){
    return a.f<b.f;
}
void solve(){
    int N,f_l,s_l,answer = 1;
    cin>>N;
    f_l = N;
    vector<ranks> temp(N);
    for(int i=0;i<N;++i){
        cin>> temp[i].f>> temp[i].s;
    }
    sort(temp.begin(),temp.end(),cmp);
    s_l = temp[0].s;
    for(int i=0;i<N;++i){
        ranks a = temp[i];
        if(a.s < s_l){
            s_l = a.s;
            answer++;
        }
    }
    
    cout<<answer<<"\n";
}


int main(void){
    int T;
    cin>>T;
    while(T--){
        solve();
    }
}