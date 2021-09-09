#include <string>
#include <vector>
using namespace std;


vector<int> answer;
//orient 위 : 1, 밑 : 2, 왼쪽 :3 , 오른쪽 : 4
void BFS(vector<string> &grid, int s_x, int s_y, int x, int y, int orient, int size){
    printf("%d, %d, %d, %d, orient = %d, size = %d \n", s_x, s_y, x,y,orient,size);
    if(size!= 0 && s_x == x && s_y == y) {
        answer.push_back(size);
        return;
    }
    int n_x = x,n_y = y,n_ori = 0;
    size += 1;
    switch (orient)
    {
    case 1: // 위쪽에서 왔을때
        switch (grid[x][y])
        {
        case 'S':
            n_x += 1; // 밑으로 
            n_ori = orient;
            break;
        case 'R':
            n_y += -1; // 왼쪽으로
            n_ori = 4; 
            break;
        case 'L':
            n_y += 1; // 오른쪽으로 
            n_ori = 3; 
            break;
        }
        break;
    case 2: // 밑에서 왔을때
        switch (grid[x][y])
        {
        case 'S':
            n_x -= 1; // 위쪽으로
            n_ori = orient;
            break;
        case 'R':
            n_y += 1; // 오른쪽으로
            n_ori = 3; 
            break;
        case 'L':
            n_y += -1; // 왼쪽으로
            n_ori = 4; 
            break;
        }
        break;
    case 3: // 왼쪽에서 왔을때
        switch (grid[x][y])
        {
        case 'S':
            n_y += 1; // 오른쪽으로
            n_ori = orient; 
            break;
        case 'R':
            n_x += 1; // 밑으로
            n_ori = 1;
            break;
        case 'L':
            n_x += -1;// 위쪽으로
            n_ori = 2;
            break;
        }
        break;
    case 4: // 오른쪽에서 왔을때
        switch (grid[x][y])
        {
        case 'S':
            n_y += -1; // 왼쪽으로
            n_ori = orient; 
            break;
        case 'R':
            n_x += -1;// 위쪽으로
            n_ori = 2;
            break;
        case 'L':
            n_x += 1; // 밑으로
            n_ori = 1;
            break;
        }
        break;
    }

    if(n_x == -1) n_x = grid.size()-1;
    if(n_y == -1) n_y = grid[0].size()-1;
    if(n_x == grid.size()) n_x = 0;
    if(n_y == grid[0].size()) n_y = 0;
    BFS(grid, s_x, s_y, n_x, n_y, n_ori, size);
}


vector<int> solution(vector<string> grid) {
    for(int i=0;i<grid.size();++i){
        for(int j=0;j<grid[i].size();++j){
            for(int k=0;k<4;++k){
                BFS(grid, i, j, i, j, k, 0);
            }
        }
    }
    for(auto a : answer){
        printf("%d ,",a);
    }
    printf("\n");
    return answer;
}

int main(void){
    vector<string> grid = {"R","R"};
    for(int i=0;i<grid.size();++i){
        for(int j=0;j<grid[i].size();++j){
            for(int k=0;k<4;++k){
                BFS(grid, i, j, i, j, k, 0);
            }
        }
    }
    for(auto a : answer){
        printf("%d ,",a);
    }
    printf("\n");
}