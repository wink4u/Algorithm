def solution(n, times):
    answer = 0
    times.sort()

    def check(people, resTime, times):
        cnt = 0

        for time in times:
            cnt += resTime // time

        return True if cnt >= people else False

    def binary(people, times):
        l = 1
        r = people * times[-1]
        minTime = 1e19

        while l <= r:
            mid = (l + r) // 2

            if check(people, mid, times):
                minTime = mid
                r = mid - 1
            else:
                l = mid + 1

        return minTime

    answer = binary(n, times)

    return answer