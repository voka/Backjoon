#include<iostream>
#include<algorithm>
using namespace std;
int ary[100001],temp,N;
int main(void){
    cin>>N;
    int cur = 0;
    for(int i=1;i<=N;++i){
        cin>>temp;
        auto it = lower_bound(ary+1,ary+cur+1,temp);
        *it = temp;
        if(it == ary + cur + 1)
            cur++;
    }
    cout<<N-cur<<"\n";
    return 0;
}