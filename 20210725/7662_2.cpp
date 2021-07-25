#include<map>
#include<queue>
#include<iostream>
using namespace std;
void solve(){
    priority_queue<long long int> max_;
    priority_queue<long long int,vector<long long int>,greater<long long int>> min_;
    map<long long int,int> nums;
    int coms,cnt=0;
    char com;
    long long int num;
    cin>>coms;
    while(coms--){
        cin>>com>>num;
        switch (com)
        {
        case 'I':
            if(nums[num] == 0) {
                max_.push(num);
                min_.push(num);
            }
            cnt++;
            nums[num] += 1;
            break;
        
        case 'D':
            if(!cnt) break;
            else{
                if(num > 0){
                    long long int a = max_.top();
                    while(1){
                        if(nums[a] > 0){
                            if(nums[a] - 1 == 0) max_.pop();
                            nums[a]--;
                            break;
                        }
                        else{
                            max_.pop();
                            a = max_.top();
                        }
                    }
                        
                }
                else{
                    long long int a = min_.top();
                    while(1){
                        if(nums[a] > 0){
                            if(nums[a] - 1 == 0) min_.pop();
                            nums[a]--;
                            break;
                        }
                        else{
                            min_.pop();
                            a = min_.top();
                        }
                    }
                }
                cnt--;
            }
            break;
        default:
            break;
        }
    }
    
    if(cnt == 0){
        cout<<"EMPTY\n";
    }
    else{
        cout<<max_.top()<<" "<<min_.top()<<"\n";
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