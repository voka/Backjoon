#include <string>
#include <vector>
#include <algorithm>
using namespace std;


vector<int> left_min_value(10000001);
vector<int> right_min_value(10000001);
void set_min_value(vector<int> &arr){
    left_min_value[0] = arr[0]; // 왼쪽 기준값
    for(int i=1;i<arr.size();++i){
         // 현재까지의 최소값보다 작은 숫자가 발견되면 해당 숫자로 교체
        if(left_min_value[i-1] > arr[i]) left_min_value[i] = arr[i];
        else left_min_value[i] = left_min_value[i-1]; // 아니면 현재까지의 최소값 입력
    }
    right_min_value[arr.size()-1] = arr[arr.size()-1]; // 오른쪽 기준값
    for(int i=arr.size()-2;i>=0;--i){
         // 현재까지의 최소값보다 작은 숫자가 발견되면 해당 숫자로 교체
        if(right_min_value[i+1] > arr[i]) right_min_value[i] = arr[i];
        else right_min_value[i] = right_min_value[i+1];// 아니면 현재까지의 최소값 입력
    }
}

int solution(vector<int> a) {
    set_min_value(a);
    int as = a.size(),answer=0;
    if(as <= 3) answer = as;
    else{
        for (int i = 0; i < as; i++) {
            if (a[i] <= left_min_value[i] || a[i] <= right_min_value[i]) 
                answer++;
        }
    }
    return answer;
}