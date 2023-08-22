import sys
from collections import deque
import copy
input = sys.stdin.readline

# N극은 0 S극은 1

topni = []

for i in range(4):
    q = deque(list(input().rstrip()))
    topni.append(q)

# 회전 시키는 횟수
K = int(input())

# dx로 옆에 있는 톱니바퀴로 이동
dx = [-1, 1]

# K번 회전시킴
# visit배열을 통해 회전시켰는지 판단을하고 입력값을 받을때마다 초기화 시켜줌
for _ in range(K):
    q = deque()
    visit = [0] * 4
    num, dir = map(int, input().split())
    visit[num - 1] = 1
    q.append((num - 1, dir))
    # example은 topni를 복사해서 톱니의 극성을 비교할 때 초기에 옆 톱니와의 극성이
    # 어떻게 되어있는지를 판단하기 위해 deepcopy를 사용, 그리고 topni를 움직임으로써
    # 새로 할당하기 위해 사용
    example = copy.deepcopy(topni)

    while q:
        for _ in range(len(q)):
            number, direction = q.popleft()
            # for문을 통해 옆 톺니로 이동
            for d in range(2):
                next = number + dx[d]
                # 톱니의 개수와 움직였는지 확인
                if next >= 0 and next <= 3 and not visit[next]:
                    visit[next] = 1
                    # 현재 톱니와 이동한 톱니와 비교를 통해 어떤 인덱스를 비교할지 판단
                    # direction에 따라 회전을 어떻게 할지 로직을 구성
                    if next < number:
                        if example[number][6] != example[next][2]:
                            if direction == -1:
                                temp = topni[next].pop()
                                topni[next].appendleft(temp)
                                q.append((next, 1))
                            elif direction == 1:
                                temp = topni[next].popleft()
                                topni[next].append(temp)
                                q.append((next, -1))

                    elif next > number:
                        if example[number][2] != example[next][6]:
                            if direction == -1:
                                temp = topni[next].pop()
                                topni[next].appendleft(temp)
                                q.append((next, 1))
                            elif direction == 1:
                                temp = topni[next].popleft()
                                topni[next].append(temp)
                                q.append((next, -1))
    # 다른 톱니들을 회전후 원래 자신의 톱니를 회전
    if dir == 1:
        tmp = topni[num - 1].pop()
        topni[num - 1].appendleft(tmp)
    else:
        tmp = topni[num - 1].popleft()
        topni[num - 1].append(tmp)

ans = 0
ans_list = [1, 2, 4, 8]
for i in range(4):
    if topni[i][0] == '1':
        ans += ans_list[i]

print(ans)