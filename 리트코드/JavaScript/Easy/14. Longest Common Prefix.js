/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 1) return strs[0]

    let n = 201
    let word = ''
    for (let i = 0; i < strs.length; i++){
        if (n > strs[i].length) {
            n = strs[i].length
            word = strs[i]
        }
    }

    if (n === 0) return ""
    let ans = word;

    for (let i = 0; i < n; i++){
        let flag = 0

        for (let j = 0; j < strs.length; j++) {
            if (word[i] !== strs[j][i]) {
                flag = 1
                break
            }
        }

        if (flag) {
            ans = word.slice(0, i)
            break
        }
    }

    return ans
};