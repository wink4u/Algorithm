/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const ans = []

    const check = (str, o, c) => {
        if (str.length === 2 * n) {
            ans.push(str)
            return
        }

        if (o < n) check(str + '(', o + 1, c)
        if (c < o) check(str + ')', o, c + 1)
    }

    check('', 0, 0)

    return ans
};