# 오르막 수가 되기 위해서는 끝자리가 추가될 숫자보다 작거나 같아야 합니다.
# 끝자리 수  <= 맨끝에 추가할 수
# ex : 끝자리가 4일떄 
# ~44, ~45, ~46, ~47, ~48, ~49 이런식으로 6개를 추가할 수 있습니다.
N = int(input())
mylib = {} # N : [N 자리 수 중 끝자리가 1 ~ 9 인 수의 개수]
mylib[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2,N+1):
    cur_list = [1]
    for j in range(2,11):
        cur_list.append(sum(mylib[i-1][:j]))
    mylib[i] = cur_list
print(sum(mylib[N])%10007)


# 문제 잘 읽읍시다. 10007로 나눈 나머지를 간과해서 처음에 틀렸어요... 