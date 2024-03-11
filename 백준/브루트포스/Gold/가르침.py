import sys
input = sys.stdin.readline

N, K = map(int, input().split())

res = 0

if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

words = [set(input().strip()) for _ in range(N)]
abc = [0] * 26

for alpha in ['a', 'c', 'i', 'n', 't']:
    abc[ord(alpha) - ord('a')] = 1

def check(idx, cnt):
    global res

    if cnt == K - 5:
        isRead = 0
        for word in words:
            flag = True
            for w in word:
                if not abc[ord(w) - ord('a')]:
                    flag = False
                    break

            if flag:
                isRead += 1

        res = max(res, isRead)
        return

    for i in range(idx, 26):
        if not abc[i]:
            abc[i] = 1
            check(i, cnt + 1)
            abc[i] = 0

check(0, 0)
print(res)