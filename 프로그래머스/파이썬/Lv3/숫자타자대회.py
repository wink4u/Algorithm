def solution(numbers):
    weights = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
    ];

    n = len(numbers)
    dp = [[[1e7] * 10 for _ in range(10)] for _ in range(n + 1)]
    dp[0][4][6] = 0

    for idx in range(n):
        num = int(numbers[idx])

        for i in range(10):
            for j in range(10):
                if i == j or dp[idx][i][j] == 1e7:
                    continue

                if dp[idx + 1][i][num] > dp[idx][i][j] + weights[num][j]:
                    dp[idx + 1][i][num] = dp[idx][i][j] + weights[num][j]

                if dp[idx + 1][num][j] > dp[idx][i][j] + weights[i][num]:
                    dp[idx + 1][num][j] = dp[idx][i][j] + weights[i][num]

    answer = 1e7
    for i in range(10):
        for j in range(10):
            answer = min(answer, dp[n][i][j])

    return answer