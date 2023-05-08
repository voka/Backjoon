import sys
sys.setrecursionlimit(10**5)
ip = sys.stdin.readlines
inputs = ip()
nodes = [[-2, -1, -1, -1] for _ in range(10001)]


def last(idx):
    [p, l, r, v] = nodes[idx]
    if l != -1:
        last(l)
    if r != -1:
        last(r)
    print(v)


def make_tree(parent, idx, val):
    [p, l, r, v] = nodes[parent]
    if v < val:
        if r != -1:  # 오른쪽 자식이 있음
            make_tree(r, idx, val)
        else:
            nodes[idx][3] = val
            nodes[idx][0] = parent
            nodes[parent][2] = idx
            return
    else:
        if l != -1:  # 왼쪽 자식이 있음
            make_tree(l, idx, val)
        else:
            nodes[idx][3] = val
            nodes[idx][0] = parent
            nodes[parent][1] = idx
            return


nodes[0][0] = -1
idx = 0  # root
for i in inputs:
    # for _ in range(9):
    # i = ip()
    cur = int(i)
    nodes[idx][3] = cur
    if idx != 0:
        make_tree(0, idx, cur)
    idx += 1
last(0)
