import sys
input = sys.stdin.readline

N = int(input())
trees = [list(map(int, input().split())) for _ in range(N)]

res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(arr, visit):
    global res
    if len(arr) == 4:
        total = 0
        for i in range(len(arr)):
            total += arr[i]
        res = max(res, total)
        return

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                a = trees[i][j]
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]

                    if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj]:
                        temp = a + trees[ni][nj]
                        visit[i][j], visit[ni][nj] = 1, 1
                        arr.append(temp)
                        check(arr, visit)
                        visit[i][j], visit[ni][nj] = 0, 0
                        arr.pop()
                        
if N == 2:
    for i in range(N):
        res += sum(trees[i])
else:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    check([], visited)
    
print(res)
    