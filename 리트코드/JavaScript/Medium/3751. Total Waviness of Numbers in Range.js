/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var totalWaviness = function(num1, num2) {
    let ans = 0

    const check = (num) => {
        const s = String(num).split('')
        const len = s.length
        
        let cnt = 0

        for (let i = 1; i < len - 1; i++){
            const [prev, now, nxt] = s.slice(i - 1, i + 2).map(Number)

            if ((prev < now && now > nxt) || (prev > now && now < nxt)) {
                cnt++
            }
        }

        return cnt
    }

    for (let i = num1; i <= num2; i++){
        ans += check(i)

    }

    return ans
};

