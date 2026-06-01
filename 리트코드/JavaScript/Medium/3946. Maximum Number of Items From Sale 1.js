/**
 * @param {number[][]} items
 * @param {number} budget
 * @return {number}
 */
var maximumSaleItems = function(items, budget) {
    const n = items.length;
    const freeCount = Array(n).fill(0);

    for (let i = 0; i < n; i++) {
        const factorI = items[i][0];

        for (let j = 0; j < n; j++) {
            if (i === j) continue;

            const factorJ = items[j][0];

            if (factorJ % factorI === 0) {
                freeCount[i]++;
            }
        }
    }

    const dp = Array(budget + 1).fill(0);

    for (let i = 0; i < n; i++) {
        const price = items[i][1];
        const bonus = freeCount[i];


        for (let b = budget; b >= price; b--) {
            dp[b] = Math.max(dp[b], dp[b - price] + 1 + bonus);
        }

        for (let b = price; b <= budget; b++) {
            dp[b] = Math.max(dp[b], dp[b - price] + 1);
        }
    }

    return dp[budget];
};