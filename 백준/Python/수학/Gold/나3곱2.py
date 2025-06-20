import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(n):
    check = [arr[i]]
    visit = [0] * n
    visit[i] = 1
    idx = 0
    while True:
        if idx == n - 1:
            flag = 2
            break
        cnt = 0
        for j in range(n):
            if not visit[j]:
                if (check[idx] % 3 == 0 and check[idx] // 3 == arr[j]) or check[idx] * 2 == arr[j]:
                    check.append(arr[j])
                    visit[j] = 1
                    idx += 1
                    break
            cnt += 1

        if cnt == n:
            flag = 1
            break

    if flag == 2:
        print(*check)
        break
