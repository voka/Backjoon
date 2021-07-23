/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int Answer;

int main()
{
	int T, test_case;
	/*
	   The freopen function below opens input.txt file in read only mode, and afterward,
	   the program will read from input.txt file instead of standard(keyboard) input.
	   To test your program, you may save input data in input.txt file,
	   and use freopen function to read from the file when using cin function.
	   You may remove the comment symbols(//) in the below statement and use it.
	   Use #include<cstdio> or #include <stdio.h> to use the function in your program.
	   But before submission, you must remove the freopen function or rewrite comment symbols(//).
	 */	

	// freopen("input.txt", "r", stdin);
    
	cin >> T;
	for(test_case = 0; test_case  < T; test_case++)
	{
	    int N,K;
        vector<int> A,B;
        cin >> N >> K;
        cout<<N<<", "<<K<<"\n";
        for(int i=0;i<N;++i){
            int a;
            cin >> a;
            A.push_back(a);
        }
        for(int i=0;i<N;++i){
            int b;
            cin >> b;
            A.push_back(b);
        }
        sort(A.begin(),A.end());
        sort(B.begin(),B.end());
		reverse(B.begin(),B.begin() + N);
		Answer = 0;
		
		for(int i=0;i<N;++i){
		    Answer = max(Answer,A[i] + B[i]);
		}
		/////////////////////////////////////////////////////////////////////////////////////////////
		/*
		   Implement your algorithm here.
		   The answer to the case will be stored in variable Answer.
		 */
		/////////////////////////////////////////////////////////////////////////////////////////////
		
		// Print the answer to standard output(screen).
		cout << "Case #" << test_case+1 << endl;
		cout << Answer << endl;
	}

	return 0;//Your program should return 0 on normal termination.
}