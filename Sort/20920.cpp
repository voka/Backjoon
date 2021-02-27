#include <bits/stdc++.h>
#define sp pair<string,int>

/* 
처음에 무턱대고 map을 사용했다가 sorting할때 자꾸 에러가 나서 찾아보니 ordered std라 특정조건으로
sorting 하려면 vector나 deque로 바꿔야한다는 것을 몰랐다.   시간이 많이 걸려버렸다.. ㅜㅜ 

 */

using namespace std;

bool compare(const sp& a,const sp& b){
    if (a.second != b.second){
        return a.second>b.second;
    }else{
        if(a.first.length() != b.first.length()){
            return a.first.length()>b.first.length();
        }
        else
            return a.first<b.first; 
    }
}

void printArray(deque<sp> a){
    for(sp i : a){
        cout<< i.first<<"\n";
    }
}


int main(void){
    
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int N,M;
    map<string,int> Dtemp;
    cin>>N>>M;
    for(int i=0;i<N;++i){
        string temp;
        cin>>temp;
        if(temp.length()<M)
            continue;
        Dtemp[temp] += 1;
    }
    deque<sp> myDictionary(Dtemp.begin(),Dtemp.end());

    sort(myDictionary.begin(),myDictionary.end(),compare);

    printArray(myDictionary);

    return 0;
}