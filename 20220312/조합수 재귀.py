def comb(n,r): 
    if n < r :
        return 0
    if n == r or r == 0:
        return 1
    else:
        return comb(n-1,r-1) + comb(n-1,r)

print(comb(30,15))
