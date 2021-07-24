/*
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <iostream>
#include <map>

using namespace std;

void solve(){
    int N,Answer = 0;
    cin>>N;
    map<int,int> con;
    for(int i=0;i<N;++i){
        int x;
        cin>>x;
        con[x] += 1;
    }
    for(auto j : con){
        int k = j.second;
        int o = j.first;
        if(k&1 == 1){
            if(Answer == 0){
                Answer = o;
            }
            else{
                Answer = Answer ^ o;
            }
        }
    }
    cout<<Answer<<"\n";
    
}
int main(int argc, char** argv)
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
	int T, test_case;
	cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{

		
		cout << "Case #" << test_case+1 << endl;
		solve();
	}

	return 0;//Your program should return 0 on normal termination.
}