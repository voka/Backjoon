import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
#print(nums)

my_nums = [0,0] # max
cur_increase,cur_decrease = 1,1
for j in range(N-1):
    if nums[j] <= nums[j+1]:
        #print("increase : ", nums[j],nums[j+1])
        cur_increase += 1
    else:
        my_nums[0] = max(my_nums[0],cur_increase)
        cur_increase = 1
    if nums[j] >= nums[j+1]:
        #print("decrease : ", nums[j],nums[j+1])
        cur_decrease += 1
    else:
        my_nums[1] = max(my_nums[1],cur_decrease)
        cur_decrease = 1
my_nums[0] = max(my_nums[0],cur_increase)
my_nums[1] = max(my_nums[1],cur_decrease)
print(max(my_nums))
        