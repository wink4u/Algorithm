var cnt = 0;
function sosu(num) {
    for (let i = 2; i < Math.sqrt(num + 1); i++){
        if (num % i === 0) {
            return false;
        }
    }

    return true;
}


function combination (arr, nums, index) {
    if (arr.length === 3) {
        const sum = arr.reduce((a, b) => a + b);
        if (sosu(sum) === true) {
            cnt += 1
        }
        return;
    }

    for (let i = index; i < nums.length; i++){
        arr.push(nums[i])
        combination(arr, nums, i + 1)
        arr.pop()
    }
}

function solution(nums) {
    var answer = -1;
    combination([], nums, 0);
    return cnt;
}