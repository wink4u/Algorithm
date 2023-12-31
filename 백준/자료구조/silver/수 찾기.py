import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dic = {}
for i in numbers:
    dic[i] = 1

M = int(input())
another = list(map(int, input().split()))

for i in another:
    if dic.get(i) == 1:
        print(1)
    else:
        print(0)