import sys 
ip = sys.stdin.readline 
N,M = map(int,ip().split())

# M번 돈을 인출
# k원 인출해 사용하고, 모자라면 남은금액은 다시 넣고 k원을 다시 인출한다.
# M번을 맞추기 위해 무조건 남은 금액은 통장에 집어놓고 다시 K원을 인출한다. 
# 돈을 아끼기 위해 K를 최소화 하고 싶다. 
lst = [int(ip()) for _ in range(N)]
moneys = [0 for _ in range(10000)]
def check(money):
    tmp = money
    count = 1
    for l in lst :
        if tmp < l:
            tmp = money
            count += 1
        tmp -= l
    return count > M or money < max(lst)
start = min(lst)
end = sum(lst)
answer = 0
while start <= end:
    mid = (start+end)//2
    if check(mid):
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)