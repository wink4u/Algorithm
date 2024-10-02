import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(n)]

root = 0

for i in range(n):
    parent = arr[i]
    if parent == -1:
        root = i
    else:
        tree[parent].append(i)


delete = int(input())
cnt = 0

def dfs(p):
    global cnt
    if tree[p]:
        for child in tree[p]:
            if child != delete:
                dfs(child)
            else:
                if len(tree[p]) == 1:
                    cnt += 1
    else:
        cnt += 1


if delete == root:
    print(0)
else:
    dfs(root)
    print(cnt)
