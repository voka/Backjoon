import sys
mydict = {}
N = int(input())
tmp = list(map(int,sys.stdin.readline().split()))
for t in tmp:
    if t < 0:
        mydict[(-t,-1)] = 1 # 절대값 기준으로 정렬하기 위한 작업
    else:
        mydict[(t,1)] = 1
mydict = sorted(mydict.keys(), key = lambda x : x[0])
#print(mydict)
answer = 20000000001
min_nums =  []
pm,pn = 0,0
for minus,num in mydict: # 정렬한 후 반복문 한번만 통과하면 정답 나온다. 
    if pm == 0:
        pm,pn = minus,num
    else:
        #print(pm*pn + minus*num)
        if answer > abs(pm*pn + minus*num):
            if pm*pn < minus*num:
                min_nums = [pm*pn , minus*num]
            else:
                min_nums = [minus*num , pm*pn]
            answer = abs(pm*pn + minus*num)
    pm,pn = minus,num
print(*min_nums)
