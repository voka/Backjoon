from sys import stdin 
def sol():
    Nums = list(map(int,stdin.readline().split()))
    Nums.sort(reverse = True)
    print(Nums[2])
T = int(input())
for _ in range(T): sol()