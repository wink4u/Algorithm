import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

num = []

def dfs(depth):
    global answer
    if depth == 3:
        for i in range(N):
            target = str(arr[i][0])
            strike, ball = 0, 0

            for j in range(3):
                if int(target[j]) == num[j]:
                    strike += 1
                elif int(target[j]) in num:
                    ball += 1

            if strike != arr[i][1] or ball != arr[i][2]:
                return

        answer += 1
        return

    for i in range(1, 10):
        if i not in num:
            num.append(i)
            dfs(depth + 1)
            num.pop()

dfs(0)
print(answer)