/**
 * @param {number} n
 * @return {number}
 */
var sumAndMultiply = function(n) {
    const arr = String(n)
    const stack = []
    let sum = 0

    for (let i = 0; i < arr.length; i++){
        const v = Number(arr[i])
        if (v) {
            sum += v
            stack.push(v)
        }
    }

    return Number(stack.join('')) * sum
};