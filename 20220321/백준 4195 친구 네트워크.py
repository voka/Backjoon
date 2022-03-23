import sys
ip =  sys.stdin.readline 
T = int(ip())
while T:
    T -= 1
    M = int(ip())
    parent = [i for i in range(200001)]
    parents_dict = {}
    group_size = {}
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    def union_parent(a,b):
        fa = find_parent(a)
        fb = find_parent(b)
        if fa < fb:
            parent[fb] = fa
            group_size[fa] += group_size[fb]
            print(group_size[fa])
        else:
            parent[fa] = fb
            group_size[fb] += group_size[fa]
            print(group_size[fb])
    for i in range(M):
        a,b = ip().rstrip().split()
        if a not in parents_dict:
            parents_dict[a] = len(parents_dict)
            group_size[parents_dict[a]] = 1
        if b not in parents_dict:
            parents_dict[b] = len(parents_dict)
            group_size[parents_dict[b]] = 1
        na = parents_dict[a]
        nb = parents_dict[b]
        if find_parent(na) != find_parent(nb):
            union_parent(na, nb)
        else:
            print(group_size[find_parent(na)])