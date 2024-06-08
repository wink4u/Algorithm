import sys
input = sys.stdin.readline

# 사람의 수 N, 파티의 수 M

N, M = map(int, input().split())

people = list(map(int, input().split()))

party = []
for _ in range(M):
    party.append(list(map(int, input().split())))


print(people)
party.sort(key = lambda x : -x[0])
print(party)