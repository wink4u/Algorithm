/**
 * @param {number[]} nums
 * @return {number}
 */
var minElement = function(nums) {
    let ans = Infinity

    for (const num of nums) {
        const s = String(num)
        const v = s.split('').reduce((a, b) => Number(a) + Number(b), 0)

        ans = Math.min(ans, v)
    }

    return ans
};