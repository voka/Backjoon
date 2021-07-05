import sys
import string
arr = [0 for i in range(27)]
ans = ""
for note in sys.stdin:
    note = note.replace(" ","")
    note = list(note)[:-1]
    for i in note:
        arr[ord(i) - 97] += 1
    
key = max(arr)
for i in range(26):
    if arr[i] == key:
        ans += chr(i+97)
        
print(ans)