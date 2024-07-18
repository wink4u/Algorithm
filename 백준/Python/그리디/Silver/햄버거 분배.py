import sys
input = sys.stdin.readline

N, K = map(int, input().split())

string = input().strip()
visit = [False] * N


for i in range(N):
    now = string[i]

    if now == 'P':
        for j in range(i - K, i + K + 1):
            if 0 <= j < N:
                if string[j] == 'H' and not visit[j]:
                    visit[j] = True
                    break

print(visit.count(True))