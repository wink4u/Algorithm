/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    const alp = new Array(26).fill(0)
    let ans = 0

    for (const w of word) {
        const ascii = w.charCodeAt()
        alp[ascii - 97]++
    }

    alp.sort((a, b) => b - a)
    let cnt = 0, num = 1;

    for (let i = 0; i < 26; i++){
        ans += num * alp[i]

        cnt++
        if (cnt === 8) {
            cnt = 0
            num++
        }
    }

    return ans
};