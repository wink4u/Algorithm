/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    
    let s = '1'

    if (n === 1) return s

    for (let i = 0; i < n - 1; i++){
        const tmp = []

        const m = s.length
        let idx = 0
        let cnt = 0
        let prev = -1

        while (true) {
            if (idx === m) {
                tmp.push(String(cnt))
                tmp.push(String(prev))
                break
            }

            if (prev === -1) {
                prev = s[idx]
                cnt = 1
            } else if (prev === s[idx]) {
                cnt++
            } else {
                tmp.push(String(cnt))
                tmp.push(String(prev))
                prev = s[idx]
                cnt = 1
            }

            idx++
        }

        s = tmp.join('')
    }

    return s
};