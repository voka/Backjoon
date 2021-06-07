import random
f = open('input.txt', mode='wt', encoding='utf-8')
f.write("1000\n")
l = []
for i in range(1000):
    k = random.randrange(10000000)
    print(k)
    break
    l.append(k)
    k = str(k)
    f.write(k)
    f.write("\n")
