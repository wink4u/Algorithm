/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const n = digits.length
    const letter = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z']
    }

    const ans = []

    const dfs = (idx, arr) => {
        if (idx === n) {
            ans.push(arr.join(''))
            return
        }


        const v = letter[digits[idx]]

        for (let j = 0; j < v.length; j++){
            arr.push(v[j])
            dfs(idx + 1, arr)
            arr.pop()
        }

    }

    dfs(0, [])

    return ans
}