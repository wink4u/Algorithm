import sys
input = sys.stdin.readline

N, M = map(int, input().split())

check_ele = [list(map(int, input().split())) for _ in range(N)]
test_ele = [list(map(int, input().split())) for _ in range(M)]


check = []
test = []

for l, v in check_ele:
    for i in range(l):
        check.append(v)

for l, v in test_ele:
    for i in range(l):
        test.append(v)

total = 0
for i in range(100):
    total = max(test[i] - check[i], total)

print(total)