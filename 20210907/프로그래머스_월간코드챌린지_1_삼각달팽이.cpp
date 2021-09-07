#include <string>
#include <vector>
#include <iostream>

using namespace std;

// 출처 - https://yabmoons.tistory.com/575
vector<int> solution(int n) {
vector<vector<int>> myboard(n + 1, vector<int>(n + 1));
    vector<int> answer;
    int Max_Num = (n * (n + 1)) / 2;
    int Top = 1;
    int Bottom = n;
    int Left = 1;
    int Right = 0;
    int Num = 1;
    int State = 0;
    while (Num <= Max_Num)
    {
        switch (State)
        {
        case 0:
            for (int i = Top; i <= Bottom; i++) myboard[i][Left] = Num++;
            Top++;
            Left++;
            State = 1;
            break;

        case 1:
            for (int i = Left; i <= Bottom - Right; i++) myboard[Bottom][i] = Num++;
            Bottom--;
            State = 2;
            break;

        case 2:
            for (int i = Bottom; i >= Top; i--) myboard[i][i - Right] = Num++;
            Right++;
            Top++;
            State = 0;
            break;
        
        default:
            break;
        }
    }
 
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            answer.push_back(myboard[i][j]);
        }
    }
    return answer;
}