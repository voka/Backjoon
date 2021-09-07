#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int mul_3(int a){
    return a * 3;
}
int solution(int n) {
    vector<int> threes;
    vector<int> ans;
    int f = 1,i = 0;
    while(f <= n){
        threes.push_back(f);
        f =  mul_3(f);
        ans.push_back(0);
    }
    reverse(threes.begin(),threes.end());
    while(n>=0 && i < ans.size()){
        if(threes[i] <= n){
            n -= threes[i];
            ans[i] += 1;
        }else i++;
    }
    reverse(ans.begin(),ans.end());
    int answer = 0;
    for(int i=0;i<threes.size();++i){
        answer += threes[i] * ans[i];
    }
    return answer;
}