import sys
input = sys.stdin.readline

n = int(input())

def check(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if l == r:
            break
        # print(l, r, flag, s_count[s[l]], s_count[s[r]])
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            tmp = s[:l] + s[l + 1:]
            if tmp[:] == tmp[::-1]:
                return 1

            tmp2 = s[:r] + s[r + 1:]
            if tmp2[:] == tmp2[::-1]:
                return 1

            return 2

    return 0

for _ in range(n):
    s = input().strip()
    print(check(s))

