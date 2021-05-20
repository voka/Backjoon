#include <iostream>
#include <algorithm>
using namespace std;
 
int electric_line[1001]={0,}, LCS[1001], temp[1001], lenght, N;

void backtrace(int idx, int num) {
    if(idx == 0)
        return;
    if(temp[idx] == num) {
        backtrace(idx - 1, num - 1);
        cout << electric_line[idx] << " ";
    }
    else {
        backtrace(idx - 1, num);
    }
}
void prints(int cur){
    for(int i=0;i<=cur;++i){
        cout<<"i == " <<i<<", electric_line == "<<electric_line[i]<<" \n";
    }
    cout<<"\n";
}
int main() {
    ios_base::sync_with_stdio(false);
    cin >> N;
    for(int i = 0; i < N; ++i) {
        int t;
        cin>>t;
        cin >> electric_line[t-1];
    }
    prints(N);
    for(int i = 0; i < N; ++i){
        auto pos = lower_bound(LCS, LCS + lenght, electric_line[i]);
        *pos = electric_line[i];
        temp[i] = distance(electric_line+1,pos);
        if(pos == LCS + lenght)
            lenght++;
    }
    cout << lenght << "\n";
    backtrace(N,lenght);
    return 0;
}

