mystr = input()
new_str = []
for letter in mystr:
    if((letter <= 'Z') & (letter >= 'A')):
        new_str.append(letter)
flag = 0
if(new_str.count('U') >= 1):
    id = new_str.index('U') + 1
    new_str = new_str[id:]
    #print(new_str)
    if(new_str.count('C') >= 1):
        id = new_str.index('C') + 1
        new_str = new_str[id:]
        #print(new_str)
        if(new_str.count('P') >= 1):
            id = new_str.index('P') + 1
            new_str = new_str[id:]
            #print(new_str)
            if(new_str.count('C') >= 1):
                flag = 1
if(flag == 1):
    print("I love UCPC")
else :
    print("I hate UCPC")

