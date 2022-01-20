from sys import stdin
N,T_len = map(int,stdin.readline().split())
Locations = list(map(int,stdin.readline().strip().split()))
Locations.sort()
T_num = 0
cur_s = Locations[0]
cur_e = cur_s + T_len
for i in range(N):
    if cur_s <= Locations[i] < cur_e:
         continue
    else:
        cur_s = Locations[i]
        cur_e = cur_s + T_len
        T_num += 1
print(T_num+1)
"""
99%에서 자꾸 틀렸다고 하는데 이유를 모르겠음 .. 
그래서 locations 길이 말고 테이프길이를 통해 구하는 방식으로 변경
cur_s = Locations[0]
cur_e = Locations[0]
for i in range(N):
    cur_e = Locations[i]
    #print(T_num)
    if i == N-1:
        if (cur_e - cur_s) <= (T_len-1):
            T_num += 1
        else:
            T_num += 2
        break
    #print(cur_s,cur_e)
    if (cur_e - cur_s) > (T_len-1):
        T_num += 1
        cur_s = Locations[i]
print(T_num)
"""