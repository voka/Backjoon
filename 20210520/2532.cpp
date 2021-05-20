#include<iostream>
#include<algorithm>
using namespace std;
struct agung{
    int x1;
    int x2;
    static struct _compare{
        bool operator ()(agung a , agung b){
            //if(a.x1 < b.x1 && a.x2 > b.x2) return false;
            //if(a.x1 == b.x1 && a.x2 > b.x2) return false;
            //if(a.x1 < b.x1 && a.x2 == b.x2) return false;
            if(a.x1 <= b.x1 && a.x2 >= b.x2 &&!(a.x1 == b.x1 && a.x2==b.x2)){
                return true;
            }
            return false;
        } 
    }compare;
};
int main(void){
    int N;
    cin>>N;
    int cur=0,trash;
    agung last;
    agung temp[100001] = {0,};
    for(int j=0;j<N;++j){
        cin>>trash>>last.x1>>last.x2;
        auto it = lower_bound(temp+1,temp+cur+1,last,agung::compare);
        *it = last;
        if(it == temp + cur + 1){
            cout<<last.x1<<", "<<last.x2<<"\n";
            cur++;
        }
    }  
    cout<<cur<<"\n";
}