import sys
input = sys.stdin.readline

go = int(input())
N = int(input())
# 고장난 버튼을 찾기위한 리스트
nums = [0] * 10

# 고장난 버튼이있다면 확인
if N:
    ban = list(map(int, input().split()))
    for i in range(N):
        nums[ban[i]] = 1
else:
    # 고장난 버튼이 없다면, 바로 누르던가 기존 채널에서 가든가 확인
    _min = min(len(str(go)), abs(100 - go))
    print(_min)
    exit()

# 현재 가야하는 곳이 고장난 버튼이 포함되있는지 확인
s_go = str(go)
s_flag = 1
for i in range(len(s_go)):
    if nums[int(s_go[i])]:
        s_flag = 0
        break

if s_flag:
    # 가야하는곳이 고장난 버튼이 없다면
    # 바로 누르던가 아니면, 기존 채널에서 가든가 확인
    print(min(len(s_go), abs(100 - go)))
    exit()

# 기존채널에서 가야하는 채널을 일일히
# +, - 를 통해 가는값을 default로 잡음
_min = abs(100 - go)
high = go + 1
low = go - 1

h_cnt, l_cnt = 0, 0

# 가야하는 채널을 값을 하나씩 올려서 비교
while True:
    s_high = str(high)
    flag = 0
    if high > 1000001:
        h_cnt = len(s_high) + abs(go - high)
        break

    for i in range(len(s_high)):
        if nums[int(s_high[i])]:
            high += 1
            break

        if i == len(s_high) - 1:
            h_cnt = len(s_high) + abs(high - go)
            flag = 1

    if flag:
        break

# low값이 0이 됬을때 확인하는 flag
no_low = 0
# 가야하는 채널을 값을 하나씩 내려서 비교
while True:
    s_low = str(low)
    flag = 0
    if low <= 0:
        low = 0
        # low값이 0일때
        # 고장난 버튼이 0이 포함되면 no_low를 1로 체크
        if nums[low]:
            no_low = 1
        else:
            l_cnt = 1 + abs(go - low)
        break

    for i in range(len(s_low)):
        if nums[int(s_low[i])]:
            low -= 1
            break

        if i == len(s_low) - 1:
            l_cnt = len(s_low) + abs(low - go)
            flag = 1

    if flag:
        break

# 최종 확인
if no_low:
    _min = min(_min, h_cnt)
else:
    _min = min(_min, l_cnt, h_cnt)

print(_min)