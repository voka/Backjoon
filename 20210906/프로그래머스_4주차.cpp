#include <map>
#include <string>
#include <vector>
#include <iostream>
using namespace std;


vector<string> split(string &input){
    vector<string> result;
    string temp = "";
    for(auto i : input){
        if(i == ' '){
            result.push_back(temp);
            temp = "";
        }
        else{
            temp += i;
        }
    }
    result.push_back(temp);
    return result;
}


string solution(vector<string> table, vector<string> languages, vector<int> preference) {
    map<string,int> myscore;
    for(int i=0;i<languages.size();++i){
        myscore[languages[i]] = preference[i];
        //cout<<myscore[languages[i]]<<", "<<languages[i]<<"\n";
    }
    vector<string> key;
    for(auto alpha : table){
        vector<string> temp;
        temp = split(alpha);
        int first_score = 5,score=0;
        for(int i=1;i<temp.size();++i){
            score += first_score*myscore[temp[i]];
            first_score -= 1;
        }
        key.push_back(temp[0]);
        myscore[temp[0]] = score;
    }
    string answer = "";
    int answer_score = 0;
    for(auto k : key){
        if(answer_score < myscore[k]){
            answer_score = myscore[k];
            answer = k;
        }
        else if(answer_score == myscore[k]){
            if(answer > k){
                answer = k;
            }
        }
        //cout<<k<<", "<<myscore[k]<<"\n";
    }
    return answer;
}