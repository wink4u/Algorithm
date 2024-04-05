import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(0)
else:
    value = int(input())

    vote = []
    for i in range(N - 1):
        vote.append(int(input()))

    vote.sort(key = lambda x : -x)
    ans = 0

    while True:
        if value > vote[0]:
            break

        else:
            vote[0] -= 1
            value += 1
            ans += 1

            vote.sort(key = lambda x : -x)

    print(ans)
