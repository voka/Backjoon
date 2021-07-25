#include<list>
#include<iostream>
#include<vector>
using namespace std;

void solve(){
    int N,M,K,Q,act;
    int Answer = 0;
    list<int> con;
    list<int> wait;
    cin>>N>>M>>K>>Q;
    for(int i=0;i<N;++i){
        int x;
        cin>>x;
        if(i < M) con.push_back(x);
        else wait.push_back(x);
    }
    for(int i=0;i<Q;++i){

        /*  cout<<"con  === ";
        for(auto a:con){
            cout<<a<<" ";
        }
        cout << "\n"; */

        /* cout<<"wait  === ";
        for(auto a:wait){
            cout<<a<<" ";
        }
        cout << "\n"; */
        int command;
        cin>>command;
        auto cs = con.begin();
        auto ws = wait.begin();
        auto we = wait.end();
        switch (command)
        {
        case 1:
            int L,R,plus;
            cin>>L>>R;
            L -= 1;
            R -= 1;
            plus = R - L + 1;
            R = plus;
            while(L--) cs++; // L 지점까지 이동
            while(1){ // R - L +1개 만큼 원소 삭제
                if(R <= 0) break;
                R--;
                con.erase(cs++);
            }
            while(plus--){
                if(wait.size() == 0){
                    con.insert(cs,0);
                }
                else{
                    int t = *wait.begin();
                    con.insert(cs,t);
                    wait.pop_front();
                }
            } 
            break;
        
        case 2:
            int i;
            cin>>i;
            i = i - 1;
            while(i--) cs++;
            cout<<*cs<<" ";
            break;

        case 3:
            int p,q;
            cin>>p>>q;
            while(q--) wait.insert(we,p);
            break;

        case 4:
            int t;
            cin>>t;
            while(t--) wait.pop_front();
            break;
        default:
            break;
        }
       
    }
    for(auto a:con){
        cout<<a<<" ";
    }
    cout << "\n";

}

int main(void){
    solve();
    return 0;
}