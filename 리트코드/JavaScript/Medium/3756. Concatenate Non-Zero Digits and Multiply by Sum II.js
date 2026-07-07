/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumAndMultiply = function(s, queries) {
    const N = s.length
    const M = 10n ** 9n + 7n
    const sum = Array(N + 1).fill(0)
    const check = Array.from(Array(N + 1), () => [0n, 0])
    
    const power10 = Array(N + 1).fill(1n)

    for (let i = 1; i <= N; i++){
        power10[i] = (power10[i - 1] * 10n) % M
    }

    for (let i = 0; i < N; i++) {
        const v = Number(s[i])

        if (v) {
            sum[i + 1] = sum[i] + v
            check[i + 1] = [(check[i][0] * 10n + BigInt(v)) % M, check[i][1] + 1]
        } else {
            sum[i + 1] = sum[i]
            check[i + 1] = [check[i][0], check[i][1]]
        }
    }

    const ans = []

    for (const [s, e] of queries) {
        const total = BigInt(sum[e + 1] - sum[s])
        const cnt = check[e + 1][1] - check[s][1]

        const v = (check[e + 1][0] - (check[s][0] * power10[cnt]) % M + M) % M

        const res = (v * total) % M
        ans.push(Number(res))
    }

    return ans
};