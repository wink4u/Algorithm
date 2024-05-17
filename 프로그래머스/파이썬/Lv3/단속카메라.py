def solution(routes):
    answer = 1
    routes.sort(key=lambda x: (x[0], x[1]))

    end = routes[0][1]
    for i in range(1, len(routes)):
        s, e = routes[i][0], routes[i][1]

        if end < s:
            end = e
            answer += 1

        end = min(end, e)
    return answer