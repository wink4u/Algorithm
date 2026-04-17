/**
 * @param {number[]} nums
 * @return {number}
 */
var minMirrorPairDistance = function(nums) {
    const N = nums.length
    const map = new Map()
    let ans = 100001

    nums.reverse()

    for (let i = 0; i < N; i++){

        const now = Number(String(nums[i]).split('').reverse().join(''))

        if (map.has(now)){
            ans = Math.min(ans, i - map.get(now))
        }

        map.set(nums[i], i)
    }

    return ans === 100001 ? -1 : ans
  
};