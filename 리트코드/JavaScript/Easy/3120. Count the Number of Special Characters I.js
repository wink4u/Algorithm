/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const check = {}
    let cnt = 0

    for (const w of word) {
        const v = w.charCodeAt()

        if (!check[v]) {
            check[v] = 1

            if (check[v - 32] || check[v + 32]) cnt++
        }
    }

    return cnt
};