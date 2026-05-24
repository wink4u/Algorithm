/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    const binarySearch = () => {
        let left = 0, right = nums.length - 1

        while (left <= right) {
            const mid = Math.floor((left + right) / 2)

            if (nums[mid] > target) {
                right = mid - 1
            } else if (nums[mid] < target) {
                left = mid + 1
            } else {
                return mid
            }
        }

        return left
    }

    return binarySearch()
};