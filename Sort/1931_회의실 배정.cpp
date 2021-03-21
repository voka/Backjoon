#include<stdio.h>
#include<algorithm>

using namespace std;

// https://www.acmicpc.net/problem/1931 회의실배정

struct meeting
{
    double start;
    double end;
};

bool cmp(meeting a, meeting b){
    if(a.end==b.end){
        return a.start<b.start;
    }
    return a.end<b.end;
}

void solve(){
    int N,answer=0;
    scanf("%d",&N);
    meeting temp[N+1];
    for(int i=0;i<N;++i){
        scanf("%lf%lf",&temp[i].start,&temp[i].end);
    }
    sort(temp,temp + N,cmp);
    double Last_end = 0;
    for(int i=0;i<N;++i){
        if(temp[i].start >= Last_end){
            Last_end = temp[i].end;
            answer++;
        } 
    }
    printf("%d\n",answer);
}

int main(void){
    solve();
    return 0;
}
