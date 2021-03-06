#include <bits/stdc++.h>
using namespace std;


void printArr(vector<int> a){
    auto i = a.end()-1;
    cout<<*i<<"\n";
}

void solve(){
    int N,C,M;
    scanf("%d%d",&N,&C);
    vector<int> Arr(N);
    for(int i=0;i<N;++i){
        scanf("%d",&Arr[i]);
    }
    scanf("%d",&M);
    for(int i=0;i<M;++i){
        int start,end;
        scanf("%d%d",&start,&end);
        int n = end-start+1;
        vector<int> temp(N);
        temp.assign(Arr.begin()+start-1,Arr.begin()+end);
        
        if(n&1){//홀수일때,
            int answer = 0;
            for(int j=0;j<n;++j){
                if(temp[n-1] == temp[j]) answer++;
            }
            if(answer > n/2) {
                printf("yes %d\n",temp[n-1]);
                continue;
            }
        }
        for(int j=0,k=n/2;j<n/2;++j,k++){
            if(temp[j] != temp[k])
                temp[j] = -1;
            temp[k] = -1;
        }
        int flag = 0,result = 0,count = 0,ans[C+1] = {0,};
        for(int j=0;j<n/2;++j){
            if(temp[j]!=-1) {
                ans[temp[j]]++;
            }
        }

        for(int j=0;j<=C;++j){
            if(ans[j]!=0){
                //cout<<"ans[j] : "<<ans[j]<<", j:"<<j<<"\n";
                if(ans[j] > count){
                    count = ans[j];
                    result = j;
                    flag = 0;
                }else{
                    if(ans[j]== count)
                        flag = 1;
                }
            }
        }
        if(flag != 1 && result != 0) printf("yes %d\n",result);
        else printf("no\n");
        
    }

}   

int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    solve();
    return 0;
}

