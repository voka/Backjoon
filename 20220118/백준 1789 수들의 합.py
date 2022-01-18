S = int(input())
sum_N = 1
N = 1
while True:
    if sum_N > S:
        break
    N += 1
    sum_N += N
print (N-1)