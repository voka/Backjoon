#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct info{
    double win_per;
    int win_big;
    int weights;
    int number;
};

bool cmp(info a, info b){
    if(a.win_per != b.win_per){
        return a.win_per>b.win_per ;
    }
    if(a.win_big != b.win_big){
        return a.win_big > b.win_big;
    }
    if(a.weights != b.weights){
        return a.weights > b.weights;
    }
    return a.number < b.number;
}
void print_info(info a){
    cout<<a.win_per << ", "<<a.win_big <<", "<<a.weights<<", "<<a.number<<"\n";
}


vector<int> solution(vector<int> weights, vector<string> head2head) {
    vector<int> answer;
    vector<info> my;
    for(int i=0;i<weights.size();++i){
        info temp;
        int total_stage = 0,win_num = 0, win_big = 0;
        temp.weights = weights[i];
        temp.number = i+1;
        for(int j = 0;j<head2head[i].size();++j){
            if(i == j) continue;
            switch (head2head[i][j])
            {
            case 'W':
                total_stage += 1;
                win_num += 1;
                if(weights[i] < weights[j]){
                    win_big += 1;
                }
                break;
            
            case 'L':
                total_stage += 1;
                break;
            default:
                break;
            }
            if(total_stage == 0) temp.win_per = 0;
            else temp.win_per = (double) win_num/total_stage;
            temp.win_big = win_big; 
        }
        my.push_back(temp);
    }
    sort(my.begin(),my.end(),cmp);
    for(auto k : my){
        answer.push_back(k.number);
    }
    return answer;
}

int main(void){
    return 0;
}