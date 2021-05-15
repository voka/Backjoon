#include <bits/stdc++.h>
#define ip pair<int,int>

/* 
https://www.acmicpc.net/problem/20551
계속 시간초과 떠서 뭐가 문제지,.... 하고 있다가,.. ㅋㅋㅋㅋㅋㅋㅋ
cout -> printf로 바꾸고 ㅋㅋㅋ 
 */

using namespace std;

int main(void){
    
    cin.tie(NULL);
    int N,M,question=0;
    cin>>N>>M;
    int array[N];
    for(int i=0;i<N;++i){
        cin>>array[i];
    }
    sort(array,array+N);
    for(int i=0;i<M;++i){
        scanf("%d",&question);
        auto ans = lower_bound(array,array+N,question);
        if(question != *ans) printf("-1\n");
        else printf("%d\n",ans-array);
    }
    /*  -<> 시간초과.... 30%까지만 됨...
        multimap<int,int> Array;
    deque<int> temp(N);
    for(int i=0;i<N;++i){
        cin>>temp[i];
        Array.insert(ip(temp[i],i));   
    }
    auto iter = Array.begin();
    for(int i=1;i<=N;++i){
        iter->second = i;
        iter++ ;     
    }
    for(int i=0;i<M;++i){
        scanf("%d",&question);
        int ans = Array.count(question);
        if(ans > 0){
            int index = Array.find(question) -> second;
            printf("%d\n",index-1);
        }
        else printf("-1\n");
    } */

    return 0;
}