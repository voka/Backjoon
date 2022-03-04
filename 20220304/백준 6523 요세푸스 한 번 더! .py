import sys
ip = sys.stdin.readline 

while True:
    cur = ip().strip()
    if cur == "0":
        exit()
    N,a,b = map(int,cur.split())
    cur_id = 0
    count_drink = 0
    K = (a*(cur_id*cur_id) + b) % N
    check = {}
    check[0] = 0
    while True:
        #print(check,K,cur_id)
        if check[cur_id] == 3:
            print(N - count_drink)
            break
        cur_id = K
        x2 = ((a%N)*(cur_id%N)*(cur_id%N))%N
        K = (x2 + b) % N
        if cur_id in check:
            check[cur_id] += 1
        else:
            check[cur_id] = 1
        if check[cur_id] == 2:
            count_drink += 1
        


