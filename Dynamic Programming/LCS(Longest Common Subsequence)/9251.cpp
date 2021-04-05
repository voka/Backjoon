#include<bits/stdc++.h>
using namespace std;

#define Loop(i,n) for(int i=1;i<=n;++i)
int dp[1001][1001] = {0,};

void printArr(int n,int m){
    Loop(i,n+1){
        Loop(j,m+1){
            cout<<dp[i-1][j-1]<<", ";
        }
        cout<<'\n';
    }
}

int find_LCS(string a, string b){
    //cout<<a<<", "<<b<<"\n";
    int len_a=a.size(),len_b=b.size();
    Loop(i,len_a-1){
        Loop(j,len_b-1){
            //cout<<a[i]<<", "<<b[j]<<"\n";
            if(a[i]==b[j]){
                dp[i][j] = max(dp[i-1][j-1]+1,max(dp[i-1][j],dp[i][j-1]));
            }
            else{
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
    //printArr(len_a,len_b);
    return dp[len_a-1][len_b-1];
}

int main(void){
    string a,b;
    cin >> a >> b;
    cout<<find_LCS("0"+a,"1"+b);
}