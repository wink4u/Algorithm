import sys
input = sys.stdin.readline

# 굴다리의 길이 N, 가로등의 개수 M
N = int(input())
M = int(input())

# 가로등의 위치
location = list(map(int, input().split()))
location.sort()

if M == 1:
    A = location[0] - 0
    B = N - location[0]
    print(max(A, B))

else:
    L = 1
    R = 1000000
    ans = 0
    while L <= R:
        mid = (L + R) // 2

        flag = 0
        for i in range(M):
            if i == 0:
                if location[i] + mid < location[i + 1] - mid or location[i] - mid > 0:
                    flag  = 1
                    break

            elif i == M - 1:
                if location[i] + mid < N:
                    flag = 1
                    break
            else:
                if location[i] + mid < location[i + 1] - mid:
                    flag = 1
                    break

        if flag == 1:
            L = mid + 1
        else:
            R = mid - 1
            ans = mid

    print(ans)
