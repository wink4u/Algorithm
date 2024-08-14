import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

len_a = len(a)
answer = 0

def check(s, t):
    global answer
    if len(s) == len(t):
        if t == s:
            answer = 1
        return

    if t[-1] == 'A':
        check(s, t[:-1])
    if t[0] == 'B':
        check(s, t[:0:-1])

check(a, b)
print(answer)
