#include<iostream>
#include<algorithm>
using namespace std;

int N;

int make_line[40001] = {0,};

int main(void){
    ios_base::sync_with_stdio(false);
    cin >> N;
    int cur = 0;
    for(int i = 1; i <= N; ++i) {
        int here;
        cin >> here;
        auto pos = lower_bound(make_line + 1, make_line + cur + 1, here);
        *pos = here;
        if(pos == make_line + cur + 1)
            cur++;
    }
    cout << cur;
    return 0;

}
