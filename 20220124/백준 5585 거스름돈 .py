use = int(input())
money = 1000 - use
dongs = [500,100,50,10,5,1]

counts = 0 
for i in dongs:
    if money == 0:
        break
    counts += money // i
    money %= i
print(counts) 