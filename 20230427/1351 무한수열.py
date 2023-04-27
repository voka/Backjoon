import sys
sys.setrecursionlimit(10**9)
ip = sys.stdin.readline
n, p, q = map(int, ip().split())
my_dict = {}
my_dict[0] = 1


def dfs(a):
    # print(a)
    if a in my_dict:
        return my_dict[a]
    result = dfs(int(a/p)) + dfs(int(a/q))
    my_dict[a] = result
    return result


dfs(n)

print(my_dict[n])
