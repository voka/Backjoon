#include <bits/stdc++.h>
using namespace std;


int a[301][301];

int main(void){
    int N,M,T,x,y,v,z;
    scanf("%d%d",&N,&M);
    for(int i=1;i<=N;++i){
        for(int j=1;j<=M;++j){
            scanf("%d",&a[i][j]);
        }
    }
    scanf("%d",&T);
    for(int t=0;t<T;++t){
        int answer = 0;
        scanf("%d%d%d%d",&x ,&y ,&v ,&z);
        for(int i=x;i<=v;++i){
            for(int j=y;j<=z;++j){
                answer = answer + a[i][j];
            }
        }
        printf("%d\n",answer);
    }
}