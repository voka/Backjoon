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

void find_LCS(string a, string b){
    string temp;
    int len_a=a.size(),len_b=b.size();
    Loop(i,len_a-1){
        Loop(j,len_b-1){
            if(a[i]==b[j])
                dp[i][j] = dp[i-1][j-1]+1;
            else{
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
    cout<< dp[len_a-1][len_b-1] <<'\n';
    //printArr(len_a,len_b);
    int i=len_a-1,j=len_b-1;
    while(temp.size() != dp[len_a-1][len_b-1] ){
        //cout<<a[i]<<", "<<b[j]<<'\n';
        if(a[i] == b[j]) {
            temp += b[j--];
            i--;
        }
        else{
            if(dp[i][j] == dp[i-1][j]){
                i--;
            }
            else{
                j--;
            }
        }
    }
    reverse(temp.begin(),temp.end());
    if(dp[len_a-1][len_b-1]!= 0)
        cout<<temp<<'\n';
}

int main(void){
    string a,b;
    cin >> a >> b;
    find_LCS("0"+a,"1"+b);
    return 0;
}