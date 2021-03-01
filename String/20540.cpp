#include <bits/stdc++.h>
using namespace std;

// MBTI
// https://www.acmicpc.net/problem/20540


int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    string a;
    cin>>a;
    for(auto i:a){
        switch (i)
        {
        case 'I': 
            printf("%c",'E');
            break; 
        case 'E': 
            printf("%c",'I');
            break;
        case 'S': 
            printf("%c",'N');
            break;
        case 'N': 
            printf("%c",'S');
            break;
        case 'T': 
            printf("%c",'F');
            break;
        case 'F': 
            printf("%c",'T');
            break;
        case 'J': 
            printf("%c",'P');
            break;
        case 'P': 
            printf("%c",'J');
            break;
        default:
            break;
        }
    }
    return 0;
}
