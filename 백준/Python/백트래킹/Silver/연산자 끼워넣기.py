import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
_max = -1e11
_min = 1e11

cal = list(map(int, input().split()))

def back(idx, res):
    global _max, _min
    if idx == n - 1:
        _max = max(_max, res)
        _min = min(_min, res)
        return

    if cal[0]:
        cal[0] -= 1
        back(idx + 1, res + arr[idx + 1])
        cal[0] += 1
    if cal[1]:
        cal[1] -= 1
        back(idx + 1, res - arr[idx + 1])
        cal[1] += 1
    if cal[2]:
        cal[2] -= 1
        back(idx + 1, res * arr[idx + 1])
        cal[2] += 1
    if cal[3]:
        cal[3] -= 1
        back(idx + 1, int(res / arr[idx + 1]))
        cal[3] += 1


back(0, arr[0])

print(_max)
print(_min)