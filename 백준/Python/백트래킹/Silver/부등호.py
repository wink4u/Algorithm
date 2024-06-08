import sys
input = sys.stdin.readline

N = int(input())

symbol = list(input().split())
res = []

def check(idx, arr):
    global res
    if len(arr) == N + 1:
        res.append(arr.copy())
        return

    for i in range(10):
        if arr:
            if i not in arr:
                if symbol[idx] == '>':
                    if arr[-1] > i:
                        arr.append(i)
                        check(idx + 1, arr)
                        arr.pop()
                elif symbol[idx] == '<':
                    if arr[-1] < i:
                        arr.append(i)
                        check(idx + 1, arr)
                        arr.pop()
        else:
            arr.append(i)
            check(idx, arr)
            arr.pop()

check(0, [])

res.sort()

print("".join(map(str, res[-1])))
print("".join(map(str, res[0])))

