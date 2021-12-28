#include<iostream>
#include<vector>
#include<queue>
#define MAX 1000

using namespace std;

int indegree[MAX]={0,};
vector<int> a[MAX];

void TopologySort(int N){
	int result[MAX];
	queue<int> tmp;
	// 진입차수가 0인 노드를 삽입 
	for(int i=1;i<=N;++i){
		if(indegree[i] == 0) tmp.push(i);
	}
	//모든 노드를 방문할 때 까지 반 복  
	for(int i=1;i<=N;++i){
		if(tmp.empty()) return; // 사이클 발생 !!! 
		int j = tmp.front();
		tmp.pop();
		result[i] = j;
		for(int k=0;k<a[j].size();++k){
			int t = a[j][k];
			if(--indegree[t] == 0) tmp.push(t);
		}
	}
	for(int i=1;i<=N;++i){
		printf("%d ", result[i]);
	}
}
int main(void){
	int N,M;
	scanf("%d%d",&N,&M);
	for(int i=0,j,k;i<M;++i){
		scanf("%d%d",&j,&k);
		a[j].push_back(k);
		indegree[k]++;
	} 
	
	TopologySort(N);
	
}