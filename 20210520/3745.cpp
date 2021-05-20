#include<iostream>
#include<algorithm>
using namespace std;

int main(void){
    int N;
    while(cin>>N){
        int cur=0,last=0;
        int temp[100001] = {0,};
        for(int j=0;j<N;++j){
            cin>>last;
            auto it = lower_bound(temp,temp+cur,last);
            *it = last;
            if(it == temp + cur)
                cur++;
        }  
        cout<<cur<<"\n";
    }
}