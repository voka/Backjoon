#include<algorithm>
#include<iostream>
#include<vector>
#include<math.h>
#define Loop(i,s,n) for(int i=s;i<n;++i)
#define maximum 1000000007
typedef  long ll;
using namespace std;
int N,M,K;
ll val;

ll init_tree(vector<ll> &arr, vector<ll> &tree, int node, int start, int end)
{
    if (start == end)
        return tree[node] = arr[start];
 
    int mid = (start + end) / 2;
 

    return tree[node] = ((init_tree(arr, tree, node * 2, start, mid) % maximum) * (init_tree(arr, tree, node * 2 + 1, mid + 1, end) % maximum)) % maximum;
}

ll update_tree(vector<ll> &tree, int node, int start, int end, int index)
{
    if (!(start <= index && index <= end))
        return tree[node];


    if (start == end)
        return tree[node] = val;
 
    if(start != end)
    {
        int mid = (start + end) / 2;
        return tree[node] = (update_tree(tree, node * 2, start, mid, index) * update_tree(tree, node * 2 + 1, mid + 1, end, index))%maximum;

    }
 
}

ll multiple(vector<ll> &tree, int node, int start, int end, int L, int R)
{
    if (L > end || R < start)
        return 1;
 
    if (L <= start && end <= R)
        return tree[node];
 
    int mid = (start + end) / 2;
    return multiple(tree, node * 2, start, mid, L, R) * multiple(tree, node*2+1, mid+1, end, L, R);
}


int main(void){
    cin>>N>>M>>K;
    int h = (int)ceil(log2(N));
    int tree_size = (1 << (h+1));
    vector<ll> tree(tree_size);
    vector<ll> temp_array(N);
    Loop(i,0,N){
        cin>>temp_array[i];
    }
    init_tree(temp_array,tree,1,0,N-1);
    int query = M + K;
    while(query--){
        int a;
        cin>>a;
        if (a == 1)
        {
            int b;
            scanf("%d %lld", &b, &val);
            update_tree(tree, 1, 0, N - 1, b - 1);
        }
 
        else if (a == 2)
        {
            int left, right;
            scanf("%d %d", &left, &right);
            printf("%lld\n", multiple(tree, 1, 0, N - 1, left - 1, right - 1)%maximum);
        }
    }

    return 0;
}
 