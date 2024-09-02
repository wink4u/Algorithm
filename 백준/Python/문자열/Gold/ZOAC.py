import sys
input = sys.stdin.readline

s = input().strip()

ans = [""] * len(s)

def check(start, string):
    if not string:
        return

    min_val = min(string)
    tmp = string.index(min_val)

    ans[start + tmp] = min_val
    print("".join(ans))
    check(start + tmp + 1, string[tmp+1:])
    check(start, string[:tmp])

check(0, s)
