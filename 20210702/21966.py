N = int(input())
mys = input()
if(N < 26):
    print(mys)
else:
    mid_str = mys[11:-12]
    if(mid_str.find('.') == -1):
        f_str = mys[:11]
        mid_str = "..."
        l_str = mys[-11:]
    else:
        f_str = mys[:9]
        mid_str = "......"
        l_str = mys[-10:]
    print(f_str + mid_str + l_str)