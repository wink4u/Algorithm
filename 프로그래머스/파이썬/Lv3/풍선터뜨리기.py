def solution(a):
    n = len(a)
    if n < 3:
        return n

    answer = 2
    left = [1e11] * n
    right = [1e11] * n
    for i in range(1, n - 1):
        left[i] = min(left[i - 1], a[i - 1])

    for i in range(n - 2, 0, -1):
        right[i] = min(right[i + 1], a[i + 1])

    for i in range(1, n - 1):
        if left[i] > a[i] or right[i] > a[i]:
            answer += 1
    return answer