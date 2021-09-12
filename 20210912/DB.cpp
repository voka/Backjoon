#include <map>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
using namespace std;

map<pair<string,int>, int> infos;
vector<int> solution(vector<string> info, vector<string> query) {
    map<string,int> score_info;
    vector<int> myscores;
    for(auto i : info){
        vector<string> x;
        string stringBuffer;
        istringstream ss(i);
        while (getline(ss, stringBuffer, ' ')){
            x.push_back(stringBuffer);
        }
        int score = stoi(x[4]);
        string lan[2] = {x[0],"-"};
        string position[2] = {x[1],"-"};
        string age[2] = {x[2],"-"};
        string food[2] = {x[3],"-"};
        if(score_info[x[4]] == 0) {
            score_info[x[4]] = 1;
            myscores.push_back(score);
        }
        string key;
        for(int i=0;i<2;++i){
            for(int j=0;j<2;++j){
                for(int u=0;u<2;++u){
                    for(int k=0;k<2;++k){
                        //cout<<i<<j<<u<<k<<"\n";
                        key = lan[i] +" and "+ position[j]+" and " + age[u]+" and " + food[k];
                        if(infos[{key,score}] == 0) infos[{key,score}] = 1;
                        else infos[{key,score}]++;
                    }
                }
            }  
        }/*
        for(auto k : infos){
            cout<<k.first<<" , "<<k.second.first<<" : "<<k.second.second<<"\n";
        }*/
    }
    sort(myscores.begin(),myscores.end());
    int cnt = 0;
    string pre = "";
    for(auto k : infos){

        if(pre == k.first.first){
            infos[{pre,k.first.second}] += cnt;
        }
        else{
            cnt = 0;
        }
        cnt += k.second;
        pre = k.first.first;

    }
    int m_size = myscores.size();
    vector<int> answer;
    for(auto a : query){
        string sc = "";
        int i;
        for(i=a.size()-1;;--i){
            sc = a[i] + sc ; 
            if(a[i-1] == ' ') break;
        }
        string msq = a.substr(0,i-1);
        int tar_sc = stoi(sc);
        int k = lower_bound(myscores.begin(),myscores.end(),tar_sc) - myscores.begin();
        int ans = 0;
        for(;k<m_size;++k){
            ans += infos[{msq,myscores[k]}];
        }
        answer.push_back(ans);
    }
    return answer;
}