/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    const answer = []
    const num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    const [l, h] = [String(low).length, String(high).length]

    let start = l
    while (true) {
        if (start > h) break

        let flag = 0

        for (let i = 0; i <= 9 - start; i++) {
            const v = Number(num.slice(i, i + start).join(''))
            
            if (v > high) {
                flag = 1
                break
            }
            
            if (v >= low) answer.push(v)
        }

        if (flag) break

        start++
    }

    return answer
};