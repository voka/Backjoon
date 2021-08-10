#include <string>
#include <vector>
#include <iostream>
#include <list>
using namespace std;
string solution(int n, int k, vector<string> cmd) {
    list<int> my;
    list<int>::iterator recent_m;
    int recent;
    list<pair<list<int>::iterator,int>> delete_list;
    string answer = "";
    for(int i=0;i<n;++i){
        my.push_back(i);
        answer += 'X';
    }
    auto id = my.begin();
    k += 1;
    while(--k){
        id++;
    }
    for(auto c : cmd){
        char command;
        int num;
        if(c.size() > 1){
            string a;
            command = c[0];
            for(int i=1;i<c.size();++i){
                a += c[i];
            }
            num = stoi(a) + 1;
        }
        else{
            command = c[0];
        }
        switch (command)
        {
        case 'U':
            while(--num){
                --id;
            }
            break;
        
        case 'D':
            while(--num){
                ++id;
            }
            break;
        
        case 'C':
            recent = *id;
            id = my.erase(id);
            recent_m = id;
            delete_list.push_front({recent_m,recent});
            if(id == my.end()){
                --id;
            }
            break;
        
        case 'Z':
            my.insert((*delete_list.begin()).first,(*delete_list.begin()).second);
            delete_list.pop_front();
            break;
        
        default:
            break;
        }
        
        /* cout<<"cur == "<<*id<<"\n";
        for(auto k : my){
            cout<<k<<" ";
        }
        cout<<"\n\n"; */
    }
    for(auto k : my){
        answer[k] = 'O';
    }
    cout<<"\n";
    return answer;
}