import sys
input = sys.stdin.readline

# N명의 회원 M개의 친분
N, M = map(int, input().split())

# N명의 회원들이 각자 들수 있는 weight list
weight = [0] + list(map(int, input().split()))
# 친분관계를 표시하기 위한 node 배ㅕㅇㄹ
node = [[] for _ in range(N + 1)]

for _ in range(M):
  # 인접 리스트? 로 구성
  a, b = map(int, input().split())
  node[a].append(b)
  node[b].append(a)

# 서로 최고라는 사람의 숫자
cnt = 0

for i in range(1, N + 1):
  # flag를 통해 최고인지 아닌지를 판단
  flag = False
  # i번째 사람의 최고 무게
  best = weight[i]
  
  for j in node[i]:
    # 친분관계 사람들중 자신보다 같거나 큰 무게를 드는사람을 판단
    if best <= weight[j]:
      flag = True
      break
  
  # 만약 자신이 최고라면 cnt += 1
  if flag == False:
    cnt += 1

print(cnt)