import sys
input = sys.stdin.readline

t, x, m = map(int, input().split())

# 지민이는 t 시간동안 금화를 주울 수 있음
# x개의 금화를 주워담을 수 있고

# m개의 몬스터
if m == 0:
    print(t * x)
else:
    d, s = map(int ,input().split())

    _min = (d - 1) // s
    for i in range(m - 1):
        d, s = map(int, input().split())

        _min = min(_min, (d - 1) // s)

    if _min == 0:
        print(_min)
    elif t > _min:
        print((_min + ((t - _min) // 2)) * x)
    else:
        print(t * x)