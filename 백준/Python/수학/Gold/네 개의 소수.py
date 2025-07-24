import sys
input = sys.stdin.readline

n = int(input())
prime = [1] * (n + 1)

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, n + 1, i):
            prime[j] = 0

prime[0] = prime[1] = 0
if n < 8:
    print(-1)
else:
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                if prime[i] and prime[j] and prime[k]:
                    left = n - (i + j + k)
                    if prime[left]:
                        print(i, j, k, left)
                        exit()

    print(-1)

