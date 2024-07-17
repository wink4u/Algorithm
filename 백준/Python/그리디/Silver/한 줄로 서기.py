import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
visit = [False] * N
res = [0] * N

visit[arr[0]] = True
res[arr[0]] = 1

for i in range(1, N):
    v = arr[i]
    cnt = 0

    for j in range(N):
        if v == 0:
            if not visit[j]:
                visit[j] = True
                res[j] = i + 1
                break
        else:
            if cnt == v:
                if not visit[j]:
                    visit[j] = True
                    res[j] = i + 1
                    break
            else:
                if not visit[j]:
                    cnt += 1

print(*res)