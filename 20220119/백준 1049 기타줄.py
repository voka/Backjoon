from sys import stdin 
# 나는 리스트 두개를 사용해서 이중반복문으로 풀었지만 
# 우선순위 큐를 두개 사용하면 맨 위쪽에 있는 것이 최소 비용일테니까 if-else문만 잘 활용한다면 시간복잡도는 늘어나도 더 간단하게 해결할 수 있다.
# 우선순위 큐 배결기반, 연결리스트 기반 시간복잡도  -> 삽입 : O(n), 삭제 O(1)
# 힙기반 -> 둘다 O(log 2 N) 
N,M = map(int,stdin.readline().split())
"""
pack_lines = []
one_lines = []
for _ in range(M):
    pack,one = map(int,stdin.readline().split())
    pack_lines.append(pack)
    one_lines.append(one)
answer = 6000*N + 1
pack_num = int(N/6)
one_num = N%6
#print(pack_num,one_num)
for six in pack_lines:
    for one in one_lines:
        answer = min(answer,six*pack_num + one*one_num, six*(pack_num+1), one*N)
print(answer)
"""
# 우선순위 큐 이용 문제풀이 
from queue import PriorityQueue
pack_que = PriorityQueue()
one_que = PriorityQueue()

for i in range(M):
    pack,one = map(int,stdin.readline().split())
    pack_que.put(pack)
    one_que.put(one)
answer = 6000*N+1
one_price = one_que.get()
pack_price = pack_que.get()
if N < 6:#개당 사는 가격, 패키지 하나 사는 가격 비교
    answer = min(one_price*N, pack_price)
else:
    pack_num = int(N/6)
    one_num = N%6
    # 패키지, 개별 각각 구매하는 비용, 패키지만 구매하는 가격, 개당 가격으로 모두 사는 가격 비교
    answer = min(pack_price*pack_num + one_price*one_num, pack_price*(pack_num+1), one_price*N)  
print(answer) 
    