#include<iostream>

using namespace std;

int main(void){
    int N,K;
    scanf("%d%d",&N,&K);
    int arr_money[N+1],result=0;
    for(int i=1;i<=N;++i){
        int temp = 0;
        scanf("%d",&temp);
        arr_money[i] = temp;
    }
    for(int i=N;i>0 || K != 0;--i){
        result += K/arr_money[i];
        K = K % arr_money[i];
    }
    cout<<result;
}