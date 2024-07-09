import sys

input = sys.stdin.readline

N = int(input())

arr = list(str(N))
result = []


def combi(s, exist):
    if len(s) == len(arr):
        temp = int(''.join(s))
        if temp > N:
            result.append(int(temp))
        return

    for i in range(len(arr)):
        if i not in exist:
            exist.append(i)
            s.append(arr[i])
            combi(s, exist)
            s.pop()
            exist.pop()


combi([], [])

result.sort()
print(result[0])