import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))
c_list = sorted(list(map(int, input().split())))

res = 1e10

def binary(arr, num):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= num:
            left = mid + 1
        else:
            right = mid

    return left

def check(al, bl, cl):
    global res

    for i in al:
        for j in bl:
            _max, _min = max(i, j), min(i, j)

            cxi = binary(cl, _max) - 1
            cni = binary(cl, _min)

            if 0 <= cxi < len(cl) and 0 <= cni <= cxi:
                res = min(res, abs(_max - _min))


check(a_list, b_list, c_list)
check(a_list, c_list, b_list)
check(b_list, c_list, a_list)

print(res)