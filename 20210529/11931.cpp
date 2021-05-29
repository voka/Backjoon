#include<iostream>
#include<algorithm>
using namespace std;
bool cmp(int x,int y){
    return x>y;
}
int arr[1000001]={0,};

int main(void)
{
    int N=0;
    cin>>N;
    int k=0;
    for(int i=0;i<N;++i){
        cin>>arr[i];
    }
    sort(arr,arr+N,cmp);
    for(int i=0;i<N;++i){
        printf("%d\n",arr[i]);
    }

    return 0;
}