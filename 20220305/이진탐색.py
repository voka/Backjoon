lst = []
for i in range(99,0,-11):
    lst.append(i)

lst.sort()
def b_search(start,end,target):
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == target:
            return mid
        if lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1 
    return None

result = b_search(0,len(lst),23)
print(result)
