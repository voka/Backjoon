#include<set>
#include<iostream>
using namespace std;
void solve(){
    multiset<long long int> nums;
    int coms,cnt=0;
    char com;
    long long int num;
    cin>>coms;
    while(coms--){
        cin>>com>>num;
        switch (com)
        {
        case 'I':
            nums.insert(num);
            break;
        
        case 'D':
            if(nums.empty()) break;
            if(num>0){
                nums.erase(nums.find(*(--nums.end())));
            }
            else{
                nums.erase(nums.find((*nums.begin())));
            }
            break;
        default:
            break;
        }
    }
    
    if(nums.size() == 0){
        cout<<"EMPTY\n";
    }
    else{
        cout<<*(--nums.end())<<" "<<*nums.begin()<<"\n";
    }
}

int main(void){
    int T;
    cin>>T;
    while(T--){
        solve();
    }
    return 0;
}