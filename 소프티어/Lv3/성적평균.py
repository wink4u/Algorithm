import sys
input = sys.stdin.readline

# N명의 학생들의 성적이 학번순서대로 주어짐
# 학번 구간 [A, B]가 주어졌을때 학생들 성적의 평균을 구해야함

# 학생수 N, 구간 수 K
N, K = map(int, input().split())

results = [0] + list(map(int, input().split()))

for i in range(K):
    A, B = map(int, input().split())
    total = 0
    people = B - A + 1
    for j in range(A, B + 1):
        total += results[j]

    print("{:.2f}".format(total / people))
