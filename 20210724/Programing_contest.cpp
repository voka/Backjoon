/*
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve(){
    int N,Answer = 0,m_num = 0;
    vector<int> con;
    cin>>N;
    for(int i=0;i<N;++i){
        int x;
        cin>>x;
        con.push_back(x);
    }
    sort(con.begin(),con.end());
    for(int i=0;i<N;++i){
        m_num = max(m_num,con[i]+N-i);
    }
    for(auto k : con){
        if(m_num<= k + N) Answer += 1;
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