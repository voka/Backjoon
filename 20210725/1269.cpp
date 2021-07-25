#include<algorithm>
#include<iostream>
#include<set>
using namespace std;

void solve(){
    int N1,N2;
    cin>>N1>>N2;
    long long int x;
    set<long long int> a;
    for(int i=0;i<N1;++i){
        cin>>x;
        a.insert(x);
    }
    for(int i=0;i<N2;++i){
        cin>>x;
        if(a.count(x)) a.erase(x);
        else a.insert(x);
    }
    cout<<a.size();

}

int main(void){
    solve();
    return 0;
}

