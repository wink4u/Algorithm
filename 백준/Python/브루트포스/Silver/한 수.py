import sys
input = sys.stdin.readline

N = int(input())

if N < 100:
    print(N)
else:
    cnt = 99

    for i in range(100, N + 1):
        s_n = str(i)

        di = int(s_n[1]) - int(s_n[0])
        flag = 0
        for j in range(2, len(s_n)):
            if di != int(s_n[j]) - int(s_n[j - 1]):
                flag = 1
                break

        if not flag:
            cnt += 1

    print(cnt)