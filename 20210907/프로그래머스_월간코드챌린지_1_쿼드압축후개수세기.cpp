#include <string>
#include <vector>

using namespace std;
int zero=0,one=0;
void press(vector<vector<int>> &arr, int start_x, int end_x, int start_y, int end_y){
    int flag = 0, divide_flag = 0, all_num = arr[start_x][end_y];
    int temp_o=0,temp_z = 0;
    printf("x = %d, y = %d\n", end_x, end_y);
    if(end_x - start_x + 1== 2){
        flag = 1;
    }
    for(int i=start_x;i<=end_x;++i){
        for(int j=start_y;j<=end_y;++j){
            if(arr[start_x][end_y] != arr[i][j]){
                divide_flag = 1;
            }
            if(arr[i][j]) temp_o++;
            else temp_z++;
        }
    }
    if(divide_flag){
        if(flag){
            zero += temp_z;
            one += temp_o;
        }
        else{
            int mid_x = (start_x + end_x+1)/2;
            int mid_y = (start_y + end_y+1)/2;
            press(arr,start_x,mid_x-1,start_y,mid_y-1);
            press(arr,mid_x,end_x,start_y,mid_y-1);
            press(arr,start_x,mid_x-1,mid_y,end_y);
            press(arr,mid_x,end_x,mid_y,end_y);
        }
    }
    else{
        if(all_num) one++;
        else zero++;
    }
    return;
    
}

vector<int> solution(vector<vector<int>> arr) {
    
    vector<int> answer;
    for(auto j : arr)
    return answer;
}
int main(void){
    vector<vector<int>> arr = {{1,1,1,1,1,1,1,1},{0,1,1,1,1,1,1,1},{0,0,0,0,1,1,1,1},{0,1,0,0,1,1,1,1},{0,0,0,0,0,0,1,1},{0,0,0,0,0,0,0,1},{0,0,0,0,1,0,0,1},{0,0,0,0,1,1,1,1}};
    press(arr,0,arr.size()-1,0,arr.size()-1);
    printf("%d, %d", zero, one);
}