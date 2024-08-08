def solution(target):
    answer = 0

    DP = [[999999, 0] for _ in range(target + 1)]

    for i in range(1, target + 1):
        if i <= 20:
            DP[i] = [1, 1]
        elif i <= 60 and i % 3 == 0:
            DP[i] = [1, 0]
        elif i <= 40 and i % 2 == 0:
            DP[i] = [1, 0]
        elif i == 50:
            DP[i] = [1, 1]
        else:
            for j in range(1, 21):
                for k in range(1, 4):
                    if i >= j * k:
                        a, b = DP[i - j * k], DP[j * k]

                        if a[0] + b[0] < DP[i][0]:
                            DP[i] = [a[0] + b[0], a[1] + b[1]]
                            continue

                        if a[0] + b[0] == DP[i][0] and a[1] + b[1] > DP[i][1]:
                            DP[i] = [a[0] + b[0], a[1] + b[1]]
                            continue

        if i >= 50:
            a, b = DP[i - 50], DP[50]

            if a[0] + b[0] < DP[i][0]:
                DP[i] = [a[0] + b[0], a[1] + b[1]]
                continue

            if a[0] + b[0] == DP[i][0] and a[1] + b[1] > DP[i][1]:
                DP[i] = [a[0] + b[0], a[1] + b[1]]
                continue

    return DP[target]