import sys
input = sys.stdin.readline

S = input().strip()

check = set()


for i in range(len(S)):
    for j in range(i, len(S)):
        tmp = S[i:j + 1]
        check.add(tmp)

print(len(list(check)))