# meet in the middle => 한번에 연산하기 어려운 문제를 둘로 나누어 시간단축을 하는 알고리즘 
# 연습
import sys
ip = sys.stdin.readline
N,C = map(int,ip().split())
lst = list(map(int,ip().split()))
left_weight = lst[:N//2]
right_weight = lst[N//2:]

left_sum = []
right_sum = []


def binarySearch(arr,target,start,end):
    while start < end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end 

def searchAll(arr,sumarr,index,weight):
    if index >= len(arr):
        sumarr.append(weight)
        return
    searchAll(arr,sumarr,index+1,weight)
    searchAll(arr,sumarr,index+1,weight+arr[index])

searchAll(left_weight,left_sum,0,0)  
searchAll(right_weight,right_sum,0,0)  
right_sum.sort()
len_right = len(right_sum)
answer = 0
for left in left_sum:
    target = C - left
    if target < 0:
        continue
    answer += binarySearch(right_sum, target, 0, len_right)
print(answer)