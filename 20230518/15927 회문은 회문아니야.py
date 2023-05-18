import sys
ip = sys.stdin.readline
text = ip().rstrip()
my = dict()
'''
이 문제는 3가지 경우가 있다. 
1. 문자열이 모두 같은 문자로 이루어져 있을경우 -> 모든 부분 문자열이 회문
2. 주어진 문자열이 회문일 경우 -> 전체 문자열 -1 이 정답  -> Why 전체 문자열이 회문이면 거기서 한 글자라도 뺴면 회문이 성립하지 않기 때문에 
3. 주어진 문자열이 회문이 아닐경우 -> 그러면 전체 문자열의 길이가 회문이 아닌 부분 문자열의 길이가 된다. 
'''

for s in text:
    if s in my:
        my[s] += 1
    else:
        my[s] = 1

n = len(text)


def is_palindrome(text):
    start = 0
    end = n - 1
    while (start < end):
        if (text[start] != text[end]):
            return False
        start += 1
        end -= 1
    return True


if len(my) == 1:
    print(-1)
else:
    if (is_palindrome(text)):
        print(n-1)
    else:
        print(n)
