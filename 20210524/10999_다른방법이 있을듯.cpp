#include<algorithm>
#include<iostream>
#include<vector>
#include<math.h>
#define Loop(i,s,n) for(int i=s;i<n;++i)

typedef long long ll;
using namespace std;
int N,M,K;
int tree_size;

ll init_tree(vector<ll> &arr, vector<ll> &tree, int node, int start, int end)
{
    if (start == end)
        return tree[node] = arr[start];
 
    int mid = (start + end) / 2;
 
    return tree[node] = init_tree(arr, tree, node * 2, start, mid) + init_tree(arr, tree, node * 2 + 1, mid + 1, end);
}
 

void update_tree(vector<ll> &tree, int node, int start, int end, int index, ll gap)
{
    if (!(start <= index && index <= end))
        return;
    
    tree[node] += gap;
 
    if(start != end)
    {
        int mid = (start + end) / 2;
        update_tree(tree, node * 2, start, mid, index, gap);
        update_tree(tree, node * 2 + 1, mid + 1, end, index, gap);
    }
 
}

ll sum(vector<ll> &tree, int node, int start, int end, int L, int R)
{
    if (L > end || R < start)
        return 0;
 
    if (L <= start && end <= R)
        return tree[node];
 
    int mid = (start + end) / 2;
    return sum(tree, node * 2, start, mid, L, R) + sum(tree, node*2+1, mid+1, end, L, R);
}


int main(void){
    cin>>N>>M>>K;
    int h = (int)ceil(log2(N));
    tree_size = (1 << (h+1));
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
            int start,end;
            ll gap;
            scanf("%d %d %lld", &start, &end,&gap);
            Loop(i,start,end+1){
                temp_array[i - 1] += gap;
                update_tree(tree, 1, 0, N - 1, i - 1, gap);
            }
        }
 
        else if (a == 2)
        {
            int left, right;
            scanf("%d %d", &left, &right);
            printf("%lld\n", sum(tree, 1, 0, N - 1, left - 1, right - 1));
        }
    }

    return 0;
}
 