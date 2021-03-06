#include <bits/stdc++.h>
using namespace std;


void solve(){
    int N,T;
    scanf("%d",&T);
    for(int i=0;i<T;++i){
        scanf("%d",&N);
        vector<int> Arr(N+1);
        int sum=0,x=0;
        for(int i=1;i<=N;++i){
            scanf("%d",&Arr[i]);
            sum += Arr[i];
        }
        auto k = max_element(Arr.begin(),Arr.end());
        int max_e = *k,answer = k - Arr.begin();
        sort(Arr.begin(),Arr.end());
        if(Arr[N] == Arr[N-1])
            printf("no winner\n");
        else{
            if(max_e>sum/2){
                printf("majority winner %d\n",answer);
            }
            else{
                printf("minority winner %d\n",answer);
            }
        }
    }

}   

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}
