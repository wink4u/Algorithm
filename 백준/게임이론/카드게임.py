import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

if N == 1:
    print("koosaga")
else:
    cnt = 1
    flag = False

    for i in range(1, N):
        if cards[i] == cards[i - 1]:
            cnt += 1
        else:
            if cnt % 2:
                flag = True
                break

            cnt = 1

    if cnt % 2:
        flag = True

    if flag:
        print("koosaga")
    else:
        print("cubelover")