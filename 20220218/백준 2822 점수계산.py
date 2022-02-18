mydict = {}
for i in range(1,9):
    mydict[i] = int(input())
answer = sorted(mydict.items(),key=lambda x : (-x[1],x[0]))
nums = []
num = 0
for i in range(5):
    nums.append(answer[i][0])
    num += answer[i][1]
print(num)
nums.sort()
print(*nums)