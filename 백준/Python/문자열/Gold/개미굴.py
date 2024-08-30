import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().split()) for _ in range(N)]

def plus(dic, s):
    if len(s) == 0:
        return

    if s[0] not in dic:
        dic[s[0]] = {}

    plus(dic[s[0]], s[1:])

def result(dic, cnt):
    for i in sorted(dic.keys()):
        print("--" * cnt + i)
        result(dic[i], cnt + 1)

dic = {}
for i in arr:
    i = i[1:]
    plus(dic, i)

result(dic, 0)