import random
import string

num = 200000 #문자열 개수
max_len = 1001 # 문자열 최대 길이
DNA_base = list("aaaaggtttttt")
f = open('./input.txt', mode='wt', encoding='utf-8')
for j in range(0,num):
    _strlen = random.randrange(100,max_len)
    string_pool = DNA_base
    result = ""
    for i in range(_strlen):
        result += random.choice(string_pool)
    f.write(result + "\n")