/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const alp = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    let idx = 0
    let ans = 0

    while (s.length > idx) {
        const v = s[idx]
        const prev = ans

        if (idx !== s.length - 1) {
            if (v == 'I') {
                if (s[idx + 1] === 'V') ans += 4
                else if (s[idx + 1] === 'X') ans += 9
            } else if (v === 'X'){
                if (s[idx + 1] === 'L') ans += 40
                else if (s[idx + 1] === 'C') ans += 90
            } else if (v === 'C') {
                if (s[idx + 1] === 'D') ans += 400
                else if (s[idx + 1] === 'M') ans += 900
            }
        }

        idx++

        if (prev === ans ){
           ans += alp[v] 
        } else {
            idx++
        }

    }

    return ans
};