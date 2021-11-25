mstr = input()
if len(mstr) < 5:
    print("not cute")
elif mstr[-5:] == 'driip':
    print("cute")
else:
    print("not cute")