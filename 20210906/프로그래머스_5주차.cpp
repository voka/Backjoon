#include <map>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string word) {
    int answer = 0;
    int sc[5] = {781,156,31,6,1};
    map<char,int> my{{'A',0},{'E',1},{'I',2},{'O',3},{'U',4}};
    answer = word.size();
    int value[5] = {0,0,0,0,0};
    for(int i=0;i<word.size();++i){ 
        value[i] = sc[i] * my[word[i]];
        cout<<value[i]<<"\n";
    }
    return answer;
}