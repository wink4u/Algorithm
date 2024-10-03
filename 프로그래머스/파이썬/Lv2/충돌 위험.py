from collections import defaultdict


def move(p, r):
    arr = []
    now, last = 0, len(r) - 1

    if now == last:
        return [(p[r[0]][0], p[r[0]][1])]
    else:

        while now != last:
            sx, sy = p[r[now]][0], p[r[now]][1]
            ex, ey = p[r[now + 1]][0], p[r[now + 1]][1]

            while sx != ex:
                arr.append((sx, sy))
                if sx > ex:
                    sx -= 1
                else:
                    sx += 1

            while sy != ey:
                arr.append((sx, sy))
                if sy > ey:
                    sy -= 1
                else:
                    sy += 1

            now += 1

            if last == now:
                arr.append((ex, ey))

    return arr


def solution(points, routes):
    points = [0] + points
    answer = 0

    robot = []

    for i in range(len(routes)):
        robot.append(move(points, routes[i]))

    print(robot)

    robot.sort(key=lambda x: -len(x))
    _max = len(robot[0])
    crush = [[] for _ in range(_max)]

    for i in range(len(robot)):
        for j in range(len(robot[i])):
            crush[j].append(robot[i][j])

    for i in range(_max):
        arr = defaultdict(int)
        for j in range(len(crush[i])):
            arr[crush[i][j]] += 1

        value = list(arr.values())

        for j in range(len(value)):
            if value[j] > 1:
                answer += 1

    return answer