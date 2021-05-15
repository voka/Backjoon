#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std;

// https://www.acmicpc.net/problem/10814 나이순 정렬

using namespace std;
vector<pair<int, string>> v;
int main()
{
	int T, age;
	char s[50];
	scanf("%d", &T);
	while (T--) {
		scanf("%d %s",&age, &s);
		v.push_back( make_pair( age, s ) );
	}

	stable_sort(v.begin(), v.end(), [](pair<int, string> _a, pair<int, string> _b) {
		if (_a.first == _b.first) {
			return false;
		}
		return _a.first < _b.first;
		});
	
	auto iter = v.begin();
	for (pair<int, string> value : v) {
		cout << value.first << " " << value.second << "\n";
	}
	return 0;
}