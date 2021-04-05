#include<bits/stdc++.h>
using namespace std;

#define Loop(i,n) for(int i=1;i<=n;++i)
int dp[201][201][201] = {0,};

void printArr(int n,int m,int a){
    Loop(i,n+1){
        Loop(j,m+1){
            Loop(k,a+1){
                cout<<dp[i-1][j-1][k-1]<<", ";
            }
        cout<<'\n';
        }
        cout<<"\n\n";
    }
}
void find_LCS(string a, string b,string c){
    string temp;
    int len_a=a.size(),len_b=b.size(),len_c = c.size();
    Loop(i,len_a-1){
        Loop(j,len_b-1){
            Loop(k,len_c-1){
                if(a[i]==b[j]&&b[j]==c[k])
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1;
                else{
                    int ij = max(dp[i-1][j][k],max(dp[i-1][j-1][k],dp[i][j-1][k]));
                    int ik = max(dp[i-1][j][k-1],dp[i-1][j][k]);
                    int jk = max(dp[i][j-1][k],dp[i][j][k-1]);
                    dp[i][j][k] = max(ij,max(ik,jk));
                }
            }
        }
    }//printArr(len_a,len_b,len_c);
    if(dp[len_a-1][len_b-1]!= 0)
        cout<< dp[len_a-1][len_b-1][len_c-1] <<'\n';
    else cout<<0<<'\n';
    return;
}


int main(void){
    string a,b,c;
    cin >> a >> b >> c;
    find_LCS("0"+a,"1"+b,"2"+c);
    return 0;
}