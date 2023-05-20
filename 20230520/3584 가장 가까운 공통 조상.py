import sys
ip = sys.stdin.readline
T = int(ip())
# sys.setrecursionlimit(10000)


def solution():
    n = int(ip())
    nodes = [-1 for _ in range(n+1)]
    for _ in range(n-1):
        p, c = map(int, ip().split())
        nodes[c] = p
    n1, n2 = map(int, ip().split())

    def get_parent_list(idx):
        result = [idx]
        while nodes[idx] != -1:
            idx = nodes[idx]
            result.append(idx)
        return result
    n1_p = get_parent_list(n1)
    n2_p = get_parent_list(n2)
    i, j = len(n1_p)-1, len(n2_p)-1
    while (n1_p[i] == n2_p[j]):
        j -= 1
        i -= 1
    print(n1_p[i+1])
    # 밑의 방법은 메모리 오류... + 리컬젼 오류
    # visited = [0]*(n+1)
    # visited[n2] = 1
    # n2_parents = False

    # def find_child(idx):
    #     global n2_parents
    #     visited[idx] = 1
    #     for num in nodes[idx][1]:
    #         if num == n2:
    #             n2_parents = True
    #             return
    #         elif visited[num] == 0 and len(nodes[num][1]) != 0:
    #             find_child(num)

    # def goto_parent(idx):
    #     find_child(idx)
    #     if n2_parents:
    #         return idx
    #     else:
    #         return goto_parent(nodes[idx][0])
    # print(goto_parent(n1))


while T:
    T -= 1
    solution()
