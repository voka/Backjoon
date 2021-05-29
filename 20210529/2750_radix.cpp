#include<iostream>
#include<fstream>
#include<queue>
using namespace std;

queue<int> Q[10];
int N;
int arrays[1001];
int max_num = 0;
void Radix_Sort() 
{   
    for (int i = 1; i < max_num; i = i * 10)    // 1의 자리부터 10씩 곱하면서 최대자릿수 까지 반복 !
    {  
        for (int j = 0; j < N; j++)    // 모든 배열을 다 탐색하면서
        {
            int K;
            if (arrays[j] < i) K = 0;        // 만약 현재 배열의 값이 현재 찾는 자릿수보다 작으면 0 !
            else K = (arrays[j] / i) % 10;    // 그게 아니라면 위에서 말한 공식 적용 !
            Q[K].push(arrays[j]);        // Queue배열에 해당 값을 순차적으로 저장 !
        }

        int Idx = 0;
        for (int j = 0; j < 10; j++)    // 0부터 9까지 Queue에 저장된 값들을 순차적으로 빼내기 위한 반복문.
        {
            while (Q[j].empty() == 0)    // 해당 Index번호의 Queue가 빌 때 까지 반복
            {
                arrays[Idx] = Q[j].front();    // 하나씩 빼면서 배열에 다시 저장.
                Q[j].pop();        
                Idx++;
            }
        }
    }
    
    for (int j = 0; j < N; j++)    // 모든 배열을 다 탐색하면서 가중치 뺴주기
    {
        arrays[j] -= 10000;
    }
}
int main(void){
    cin>>N;
    for(int i=0;i<N;++i){
        cin>>arrays[i];
        arrays[i] += 10000;//가중치 더하기
        max_num = max(max_num,arrays[i]);
    }
    Radix_Sort();
    for(int i=0;i<N;++i){
        cout<<arrays[i]<<"\n";
    }
    return 0;
}