#include<bits/stdc++.h>
using namespace std;

int N,K;
double dor[501] = {0,};
int main(void){
    cin>>N>>K;
    for(int i=0;i<N;++i){
        cin >> dor[i];
    } 
    double answer =9999999999999;
    while(1){
        if(N<K) break;
        double K_ = (double)K;
        for(int i=0;i<N-K+1;++i){
            double expatation=0,variance=0;
            for(int j=i;j<K+i;++j){
                expatation += dor[j];
            }
            expatation /= K_;
            for(int j=i;j<K+i;++j){
                variance += (dor[j]-expatation)*(dor[j]-expatation);
            }
            //cout<<"i == "<<i<<", variance == "<<variance<<",  exp == "<<expatation<<"\n";
            if(answer == 0) answer = sqrt(variance/K_);
            else answer = min(answer,sqrt(variance/K_));
        }
        K++;
    }
    
    printf("%0.11f", answer);
}