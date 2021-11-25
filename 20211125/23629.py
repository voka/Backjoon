mydict = {
"ZERO" : "0",	
"ONE" : "1",	
"TWO" : "2",	
"THREE" : "3",	
"FOUR" : "4",	
"FIVE" : "5",	
"SIX" : "6",	
"SEVEN" : "7",	
"EIGHT" : "8",	
"NINE" : "9"
}

#mycals = {"+" : "+", "-" : "-", "x" : "*", "/" : "/", "=" : "="}

cals = input()
for i in mydict.keys():
    cals = cals.replace(i,mydict[i])

#check_cals = cals
#for i in mycals.keys():
    #check_cals = check_cals.replace(i,"")

temp_cals = cals.replace("x","*")
#print(cals,check_cals,check_cals.isdigit())

# 파이썬 나누기로 풀면 틀렸다고 나옴.
try :
    if(temp_cals[-1] == '=') : 
        myans = str(eval(temp_cals[:-1]))
        print(cals)
        for i in mydict.keys():
            myans = myans.replace(mydict[i],i)
        print(myans)
        
    else : print("Madness!") 
except :
   print("Madness!") 
