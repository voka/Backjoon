
s = "xyzzaz"
count = 0
for i in range(len(s) - 2):
    temp = s[i:i+3]
    if(temp[0] != temp[1] and temp[0]!= temp[2] and temp[1] != temp[2]) : count+=1
print(count)