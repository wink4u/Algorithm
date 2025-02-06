import sys
input = sys.stdin.readline

# 작업장의 수 N
N = int(input())
work = []
for i in range(N - 1):
  # index
  # 0 = Ai 작업장의 작업시간
  # 1 = Bi 작업장의 작업시간
  # 2 = Ai 작업장에서 B(i + 1) 작업장까지 이동시간
  # 3 = Bi 작업장에서 A(i + 1) 작업장까지 이동시간
  work.append(list(map(int, input().split())))

# 이전 A, B에서의 작업시간 
prev_a, prev_b = 0, 0
# 현재 A, B에서의 작업시간
now_a, now_b = 0, 0

for i in range(N - 1):
  # 현재 작업시간은
  # 자기라인에서 작업한 시간과 다른작업장에서 이동한 작업시간의 비교를 통해 설정
  now_a = min(work[i][0] + prev_a, work[i][1] + work[i][3] + prev_b)
  now_b = min(work[i][1] + prev_b, work[i][0] + work[i][2] + prev_a)

  # 설정된 현재 작업시간은 이전 작업시간에 값을 할당
  prev_a = now_a
  prev_b = now_b

# 마지막 A, B 작업장에서의 작업시간
A, B = map(int, input().split())

now_a += A
now_b += B

print(min(now_a, now_b))

