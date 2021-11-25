sY, sM, sD = map(int,input().split(" "))
eY, eM, eD = map(int,input().split(" "))
# get days
Y = eY - sY
M = eM - sM
D = eD - sD
total_date = Y*360 + M*30 + D

temp = M
if D < 0 :
    temp -= 1
    
total_month = Y*12 + temp
if total_month > 36 :
    total_month = 36

total_year = 0
if M < 0 or D < 0 :
    Y -= 1
for i in range(Y):
    A = int((i)/2)
    total_year += (A+15)
print(total_year,total_month)
print("{}days".format(total_date))