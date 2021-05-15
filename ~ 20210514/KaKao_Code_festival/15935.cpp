#include<bits/stdc++.h>
using namespace std;


int main(void){
    int T;
    int f,s,counts=1,num=0,minus_f = 200,minus_s = 256;
    int f_M = 500,s_M=512;
    int a[7] = {0,500,300,200,50,30,10},b[6] = {0,512,256,128,64,32};
    int dp_f1[101]={0,},dp_f2[65]={0,};
    for(int i=1,index=1,j=1;index<=21;){
        dp_f1[index++] = a[j];
        if(i == counts){
            counts = 1;
            i++;
            j++;
        }
        else{
            counts++;
        }
    }
    counts = 1;
    for(int i=1,index=1,j=1;index<=31;){
        dp_f2[index++] = b[j];
        if(i == counts){
            j++;
            counts = 1;
            i = i * 2;
        }
        else{
            counts++;
        }
    }
    cin>>T;
    while(T--){
        cin>>f>>s;
        cout<<(dp_f1[f] + dp_f2[s])*10000<<"\n";
    }
}