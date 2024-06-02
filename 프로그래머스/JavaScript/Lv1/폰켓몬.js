function solution(nums) {
    var answer = 0;

    let leng = Math.floor(nums.length / 2);
    let pick_leng = [...new Set(nums)].length;

    return leng < pick_leng ? leng : pick_leng;
}