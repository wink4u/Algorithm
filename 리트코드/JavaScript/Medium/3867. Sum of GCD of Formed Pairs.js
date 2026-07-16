/**
 * @param {number[]} nums
 * @return {number}
 */
var gcdSum = function(nums) {
    let ans = 0
    const gcd = (a, b) => (b === 0) ? a : gcd(b , a % b)
    const n = nums.length

    let mx = 0
    const prefixGcd = []
    
    for (let i = 0; i < n; i++){
        mx = Math.max(mx, nums[i])

        const v = gcd(nums[i], mx)
        prefixGcd.push(v)
    }

    let left = 0, right = n - 1
    prefixGcd.sort((a, b) => a - b)
    while (left < right) {
        const v = gcd(prefixGcd[left], prefixGcd[right])
        ans += v

        left++
        right--
    }

    return ans
};