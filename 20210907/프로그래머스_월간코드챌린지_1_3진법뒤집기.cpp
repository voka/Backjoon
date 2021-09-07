#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

int solution(int n) {
    vector<int> ans;
    while(n>0){
        ans.push_back(n%3);
        n = n/3;
    }
    int answer = 0,t=1;
    reverse(ans.begin(),ans.end());
    for(int i=0;i<ans.size();++i){
        answer += t * ans[i];
        t *= 3;
    }
    return answer;
}