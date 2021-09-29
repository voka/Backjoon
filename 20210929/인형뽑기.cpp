#include <stack>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    stack<int> haha;
    int size_ = board.size();
    int answer = 0,i;
    for(auto k : moves){
        for(i=0;i<size_;++i){if(board[i][k-1] != 0) break;}
        if(i == size_) continue;
        int target = board[i][k-1];
        board[i][k-1] = 0;
        if(haha.size() != 0){
            if(haha.top() == target){
                answer += 2;
                haha.pop();
            }
            else{
                haha.push(target);   
            }
        }
        else{
            haha.push(target);
        }
    }
    return answer;
}