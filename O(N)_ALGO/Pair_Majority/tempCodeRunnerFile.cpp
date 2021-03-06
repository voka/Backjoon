#include <bits/stdc++.h>
using namespace std;

const int MAX = 3e5 + 4;
const int SMAX = (1 << 20);

int n, qq;
vector<int> seg[1001], c[10001];
vector<int> temp;


void printA(vector<int> a){
    for(auto i : a){
        cout<<i<<" ,";
    }
    cout<<"\n";
}

void construct() {
	for (int i = SMAX / 2 - 1; i >= 1; i--) {
		seg[i] = seg[i * 2 + 1];
		seg[i].insert(seg[i].end(), seg[i * 2].begin(), seg[i * 2].end());
		sort(seg[i].begin(), seg[i].end());
	}
}

void val(int s, int e, int i=1, int ns=0, int ne=SMAX/2-1) {
	if (e < ns || ne < s) return;
	if (s <= ns && ne <= e) {
		int k = (ne - ns + 1) / 2 - 1;
		if (ns == ne) temp.push_back(seg[i][0]);
		else if (seg[i][k] == seg[i][k + 1]) temp.push_back(seg[i][k]);
		return;
	}
	int md = (ns + ne) / 2;
	val(s, e, i * 2, ns, md);
	val(s, e, i * 2 + 1, md + 1, ne);
}

int main() {
	cin >> n >> qq;
	for (int i = 1, x; i <= n; i++) {
		cin >> x;
		c[x].push_back(i);
		seg[i + 1001 / 2].push_back(x);
	}
	construct();
    for(int i=0;i<1001;++i){
        printA(seg[i]);
    }
	/* for (int i = 0, s, e; i < qq; i++) {
		cin >> s >> e;
		val(s, e);

		bool flag = false;
		for (int j : temp) {
			int t = upper_bound(c[j].begin(), c[j].end(), e) - lower_bound(c[j].begin(), c[j].end(), s);
			if (t > (e - s + 1) / 2) {
				flag = true;
				cout << "yes " << j << '\n';
				break;
			}
		}

		if (!flag) cout << "no\n";
		temp.clear();
	} */
}