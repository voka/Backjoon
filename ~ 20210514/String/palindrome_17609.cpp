#include <bits/stdc++.h>
using namespace std;

// 회문
// https://www.acmicpc.net/problem/17609
int palindrome(string a){
    int Asize = a.size();
    int right = Asize-1;
    int count = 0;
    for(int left = 0; left<Asize/2 || right>Asize/2;){
        //cout<<"left : "<<a[left]<<", right : "<<a[right]<<"\n";
        if(a[left]==a[right]){
            left++;
            right--;
        }
        else{
            if(count > 0) return 2;
            count++;
            if(a[left+1]==a[right] && a[left]==a[right-1]){
                //cout<<left+1<<", "<<right<<", "<<right - left - 1<<"\n";
                //substr한 두 문자열에 대해 재귀적으로 다시 회문 검사를 함.
                if(palindrome(a.substr(left+1,right - left - 1)) == 0 || palindrome(a.substr(left,right-left))==0){
                    return 1;
                }
            }
            if(a[left+1]==a[right]){
                left++;
            }
            else if(a[left]==a[right-1]){
                right--;
            }
            else{
                return 2;
            }
        } 
    }
    if(count != 0) return 1;
    return 0;
}

int main(void){
    int N=0;
    cin>>N;
    deque<int> answer;
    for(int i=0;i<N;++i){
        string temp = "";
        cin>>temp;
        printf("%d\n",palindrome(temp));
    }
}
