#include<deque>
#include<set>
#include<map>
#include<iostream>
#include<vector>
using namespace std;
typedef long long int lli;
typedef pair<long long int, long long int> pll;

set<pll> con;
deque<pll> wait;


void burn(){
    lli L,R;
    cin>>L>>R;
    pll f  = make_pair(L,0);
    pll s  = make_pair(R,0);
    auto it1 = lower_bound(con.begin(),con.end(),f);
    auto it2 = lower_bound(con.begin(),con.end(),s);
    /* if(it1 == it2){
        
    }
    else{
        
    } */
    cout<<(it1 == con.end())<<",  "<<it1->first<<", "<<it1->second<<'\n';
    cout<<(it2 == con.end())<<",  "<<it2->first<<", "<<it2->second<<'\n';
}

void find_i(){
    int i;
    cin>>i;
    i = i - 1;
    for(auto a:con){
        cout<<a.first<<", "<<a.second<<" ";
        if(i-- < 0 ) break;
    }
}
void solve(){
    int N,M,K,Q,act;
    int Answer = 0;
    cin>>N>>M>>K>>Q;
    int counts = 0,pre = 0;
    int id = 0;
    for(int i=0;i<N;++i){
        int x;
        cin>>x;
        if(i < M) {
            if(pre == x){
                if(i == M - 1||i - counts + 1 == 0){
                    con.insert(make_pair(i - counts + 1,counts));
                    counts = 1;
                }
                counts++;
            }
            else{
                con.insert(make_pair(i - counts + 1,counts));
                counts = 1;
            }
        }
        else {
            if(pre == x){
                counts++;
                 if(i == N - 1) wait.push_back(make_pair(x,counts));
            }
            else{
                wait.push_back(make_pair(x,counts));
                counts = 1;
            }
        }
        pre = x;
    }
    for(int i=0;i<Q;++i){
        int command;
        cin>>command;
        switch (command)
        {
        case 1:
            burn();
            break;
        case 2:
            find_i();
            break;

        case 3:
            int p,q;
            cin>>p>>q;
            wait.push_back(make_pair(p,q));
            break;

        case 4:
            lli  t;
            cin>>t;
            while(1){
                lli k = wait.front().second;
                if( t - k > 0){
                    t = t - k;
                    wait.pop_front();
                }
                else if (t - k == 0)
                {
                    t = t - k;
                    wait.pop_front();
                    break;
                }
                else{
                    k = k - t;
                    wait.front().second = k;
                    break;
                }
            }
            break;
            
        default:

            break;
        }

         cout<<"con == \n";
           for(auto a:con){
                cout<<a.first<<", "<<a.second<<" ";
            }
            cout << "\n";
            cout<<"wait == \n";
           for(auto a:wait){
                cout<<a.first<<", "<<a.second<<" ";
            }
            cout << "\n";
       
    }
    

}

int main(void){
    solve();
    return 0;
}