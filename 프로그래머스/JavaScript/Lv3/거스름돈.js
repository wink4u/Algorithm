function solution(n, money) {
    const DP = Array(n + 1).fill(0)
    DP[0] = 1

    for (let i = 0; i < money.length; i++){
        const coin = money[i];
        for (let j = coin; j < n + 1; j++){
            DP[j] += DP[j - coin]
        }
    }



    return DP[n]
}