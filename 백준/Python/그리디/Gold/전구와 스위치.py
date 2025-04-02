import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())
cs = s[:]
s2 = list(input().strip())

c = {'0' : '1', '1' : '0'}

def trans(flag, idx):
    for i in range(idx - 1, idx + 2):
        if 0 <= i < n:
            if not flag:
                s[i] = c[s[i]]
            else:
                cs[i] = c[cs[i]]


ans1, ans2 = 0, 1

def check(flag):
    global ans1, ans2

    for i in range(1, n):
        if not flag:
            if s[i - 1] != s2[i - 1]:
                trans(flag, i)
                ans1 += 1
        else:
            if cs[i - 1] != s2[i - 1]:
                trans(flag, i)
                ans2 += 1

    if not flag:
        if s != s2:
            return False
    else:
        if cs != s2:
            return False

    return True


res = -1

if check(0):
    res = ans1

trans(1, 0)

if check(1):
    if res != -1:
        res = min(res, ans2)
    else:
        res = ans2

print(res)