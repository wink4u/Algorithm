def cal(diffs, times, mid, limit):
    count = 0

    for i in range(len(diffs)):
        if mid >= diffs[i]:
            count += times[i]
        else:
            if i == 0:
                prev = 0
            else:
                prev = times[i - 1]

            r = diffs[i] - mid
            count += (times[i] + prev) * r + times[i]

        if count > limit:
            return True

    return False


def solution(diffs, times, limit):
    answer = 0
    left, right = 1, max(diffs)

    while left < right:
        mid = (left + right) // 2

        if cal(diffs, times, mid, limit):
            left = mid + 1
        else:
            right = mid

    print(mid)

    return left