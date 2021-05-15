#include<stdio.h>
#include<algorithm>

using namespace std;

// https://www.acmicpc.net/problem/100815 숫자카드

struct Point
{
    int data;
    int origin;
};


void printarray(int a[],int n){
    for(int i=0;i<n;++i) printf("%d ",a[i]);
    printf("\n");
}
void printPoint(Point a[],int n){
    for(int i=0;i<n;++i) printf("%d ",a[i].data);
    printf("\n");
}
bool cmp(Point a, Point b){
    return a.data<b.data;
}

void solve(){
    int N;
    scanf("%d",&N);
    int card[N+1];
    for(int i=0;i<N;++i){
        scanf("%d",&card[i]);
    }
    sort(card,card + N);
    int M;
    scanf("%d",&M);
    Point check[N+1];
    for(int i=0;i<M;++i){
        scanf("%d",&check[i].data);
        check[i].origin = i;
    }
    sort(check,check + M,cmp);
    int answer[M]={0,};
    //printarray(card,N);
    
    //printPoint(check,M);
    for(int i=0,j=0;;){
        if(i>=N || j >=M) break;
        if(card[i]==check[j].data){
            answer[check[j].origin] = 1;
            i++;
            j++;
        }
        else{
            if(card[i]>check[j].data) j++;
            else i++;
        }
    }
    printarray(answer,M);
}

int main(void){
    solve();
    return 0;
}
