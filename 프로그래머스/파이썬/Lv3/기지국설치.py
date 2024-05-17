def solution(n, stations, w):
    answer = 0
    start = 1
    end = 0

    r = w * 2 + 1

    for station in stations:
        end = station - w - start
        if station - w > start:
            answer += (end // r)
            if end % r:
                answer += 1
        start = station + w + 1

    if start <= n:
        end = (n + 1) - start
        answer += (end // r)
        if end % r:
            answer += 1

    return answer