/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(nums) {
    const n = nums.length
    
    if (n === 1) return true

    let cnt = 0
    let mid = nums[0]

    for (let i = 1; i < n; i++){
        if (cnt === 0) {
            if (nums[i] >= nums[i - 1]) continue

            if (i === n - 1 && n >= 3 && nums[0] < nums[i]) cnt++
            cnt++
        } else {
            if (nums[i] >= nums[i - 1]) {
                if (mid < nums[i]) cnt++
            } else {
                cnt++
            }


            if (cnt === 2) break
        }
    }

    return cnt >= 2 ? false : true
};