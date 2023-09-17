import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())
fold = list(map(int, input().split()))
cut = [list(map(int ,input().split())) for _ in range(3)]

for fold_count in fold:
    if fold_count == -1:
        n //= 2
    elif fold_count == 1:
        m //= 2

paper = [[1 for _ in range(m)] for _ in range(n)]

for i in range(len(cut)):
    x, y = cut[i]
    if 0 <= x - 1 < n and 0 <= y - 1 < m:
        paper[x - 1][y - 1] = 0

for i in range(len(fold)):
    if fold[i] == 1:
        for j in range(len(paper)):
            for k in range(len(paper[j]) - 1, -1, -1):
                paper[j].append(paper[j][k])

    elif fold[i] == -1:
        for j in range(len(paper) - 1, -1, -1):
            paper.append(paper[j])

for i in range(len(paper)):
    print(paper[i])