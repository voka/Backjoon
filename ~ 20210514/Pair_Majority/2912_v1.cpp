#include <bits/stdc++.h>
using namespace std;


void solve(){
    int N,C,M;
    scanf("%d%d",&N,&C);
    vector<int> Arr(N+1);
    for(int i=1;i<=N;++i){
        scanf("%d",&Arr[i]);
    }
    scanf("%d",&M);
    for(int i=0;i<M;++i){
        int start,end;
        scanf("%d%d",&start,&end);
        int n = end-start+1;
        vector<int> cap(M+1);
        if(n == 2) {
            printf("no\n");
            continue;
        }
        int max = 0, answer = 0;
        for(int j=start;j<=end;++j){
            cap[Arr[j]]++;
            if(cap[Arr[j]] > max && cap[Arr[j]]>n/2){
                max = cap[Arr[j]];
                answer = Arr[j];
            }
        }
        if(answer == 0) {
            printf("no\n");
        }
        else{
            printf("yes %d\n" , answer);

        }
    }

}   

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}

