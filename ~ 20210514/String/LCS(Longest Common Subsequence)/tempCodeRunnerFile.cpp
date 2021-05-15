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
    string temp;
    int maximum = 0;
    int len_a=a.size(),len_b=b.size();
    Loop(i,len_a-1){
        Loop(j,len_b-1){
            if(a[i]==b[j]){
                dp[i][j] = dp[i-1][j-1]+1;
                if(dp[i][j] > maximum){
                    temp += b[j];
                    maximum = dp[i][j];
                }
            }
            else{
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
    //printArr(len_a,len_b);
    cout<< dp[len_a-1][len_b-1] <<'\n';
    if(temp.size() != 0)
        cout<<temp<<'\n';
    return 0;
}

int main(void){
    string a,b;
    cin >> a >> b;
    if(a.size() > b.size()) find_LCS("0"+b,"1"+a);
    else  find_LCS("0"+a,"1"+b);
    return 0;
}