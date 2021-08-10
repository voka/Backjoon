#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int A = 300, B = 60, C = 10;
int answer[3] = {0,};
void solve(){
    int T;
    cin >> T;
    if(T%10 != 0){
        cout<<-1<<"\n";
        return;
    }
    int i = 0;
    while(T){
        if(T >= A){
            T = T-A;
            answer[0]++;
        }
        else if(T >= B){
            T = T-B;
            answer[1]++;
        }
        else{
            T = T-C;
            answer[2]++;

        }
    }
    cout<<answer[0]<<" "<<answer[1]<<" "<<answer[2]<<"\n";
}

int main(void){
    solve();
    return 0;
}