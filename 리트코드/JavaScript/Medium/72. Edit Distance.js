/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const n = word1.length, m = word2.length
    const dp = Array.from(Array(n + 1), () => Array(m + 1).fill(-1))
    
    function res(i, j) {
        if (i === 0) return j;
        if (j === 0) return i;
        if (dp[i][j] !== -1) return dp[i][j]

        if (word1[i - 1] === word2[j - 1]) {
            dp[i][j] = res(i - 1, j - 1)
        } else {
            dp[i][j] = 1 + Math.min(
                res(i - 1, j),
                res(i, j - 1),
                res(i - 1, j - 1)
            )
        }

        return dp[i][j]
    }

    return res(n, m)
};