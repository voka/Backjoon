#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int rest(vector<int> &arr, int index){
    int flag = 1, mynum = arr[index];
    auto my = arr.begin();
    for(auto k = arr.begin();k<arr.end();++k){
        if(*k == mynum){
            my = k;
            break;
        }
    }
    int c_l = *min_element(arr.begin(),my-1);
    int c_r = *min_element(my+1,arr.end());
    if(c_l < mynum && c_r < mynum) flag = 0;
    return flag;
}
vector<int> left_min_value,right_min_value;
void set_min_value(vector<int> &arr){
    for(int i=0;i<arr.size();++i){

    }
}

int solution(vector<int> a) {
    int as = a.size(),answer=0;
    if(as <= 3) answer = as;
    else{
        for(int i=1;i<a.size()-1;++i){
            if(rest(a,i)) answer++;
        }
    }
    return answer;
}
int main(void){
    vector<int> a = {-16,27,65,-2,58,-92,-71,-68,-61,-33};
    int as = a.size(),answer=0;
    if(as <= 3) answer = as;
    else{
        for(int i=1;i<a.size()-1;++i){
            if(rest(a,i)) answer++;
        }
    }
    printf("answer == %d",answer+2);
}