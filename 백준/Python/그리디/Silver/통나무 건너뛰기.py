import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    # print(arr)
    _max = 0

    value1 = arr[0]
    for i in range(2, N, 2):
        _max = max(_max, abs(arr[i] - value1))
        value1 = arr[i]

    if N % 2:
        value2 = arr[N - 2]
        for i in range(N - 4, -1, -2):
            _max = max(_max, abs(arr[i] - value2))
            value2 = arr[i]
    else:
        value2 = arr[N - 1]
        for i in range(N - 1, -1, -2):
            _max = max(_max, abs(arr[i] - value2))
            value2 = arr[i]

    print(_max)