#include<iostream>
#include<algorithm>
using namespace std;

int main(void){
    int T;
    cin>>T;
    for(int i=0;i<T;++i){
        int N,K,cur=0,last=0;
        int temp[100001] = {0,};
        cin>>N>>K;
        for(int j=0;j<N;++j){
            cin>>last;
            auto it = lower_bound(temp,temp+cur,last);
            *it = last;
            if(it == temp + cur)
                cur++;
        }
        cout<<"Case #"<<i+1<<"\n";
        int answer = K<=cur ? 1:0;
        cout<<answer<<"\n";
    }
}