/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const n = nums.length
    const arr = nums.map((v, idx) => [v, idx]).sort((a, b) => a[0] - b[0])
    
    let left = 0, right = n - 1

    while (left < right) {
        const sum = arr[left][0] + arr[right][0]

        if (sum === target) {
            return [arr[left][1], arr[right][1]]
        } else if (sum > target) {
            right--
        } else {
            left++
        }
    }
};