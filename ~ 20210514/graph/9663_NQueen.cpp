#include<iostream>
#include<algorithm>
using namespace std;
int N,num = 0;
int borad[16] = {0,};



bool check(int v){
    for(int i=0;i<v;++i){
        if(borad[i] == borad[v]) return false; // 
        if(abs(borad[i] - borad[v]) == v - i) return false;
    }
    return true;

}

void queen(int v){
    if(v==N) {
        num++;
    }
    else{
        for(int i=0;i<N;++i){
            borad[v] = i;
            if(check(v)){
                queen(v+1);
            }

        }
    }
}   

int main(void){
    cin>>N;
    queen(0);
    cout<<num;
}