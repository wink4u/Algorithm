import sys

input = sys.stdin.readline

# 게이트의 수
G = int(input())

# 비행기의 수
P = int(input())
gate = [i for i in range(G + 1)]
ans = 0

def find(airplane):
    if gate[airplane] == airplane:
        return airplane

    gate[airplane] = find(gate[airplane])

    return gate[airplane]

for _ in range(P):
    air = int(input())

    res = find(air)

    if res == 0:
        break

    gate[res] = gate[res - 1]
    ans += 1

print(ans)

