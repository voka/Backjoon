# 1 3 -1 4 1 7 input
"""
c-by/a = x
f - ey/d = x
c-by /a == f - ey/d
cd - dby = af - aey
cd - af = (db-ae)y
(cd - af) / (db-ae) = y
(bf - ce) / (db-ae) = x
"""
a,b,c,d,e,f = map(int,input().split())
x = (b*f - c*e)/(d*b - a*e)
y = (c*d - a*f)/(d*b - a*e)
print(int(x),int(y))