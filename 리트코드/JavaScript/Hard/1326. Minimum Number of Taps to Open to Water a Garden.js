/**
 * @param {number} n
 * @param {number[]} ranges
 * @return {number}
 */
var minTaps = function(n, ranges) {
    const reach = new Array(n + 1).fill(0)

    for (let i = 0; i <= n; i++){
        const left = Math.max(0, i - ranges[i])
        const right = Math.min(n, i + ranges[i])

        reach[left] = Math.max(reach[left], right)
    }

    let cnt = 0
    let currEnd = 0
    let nextEnd = 0

    for (let i = 0; i < n; i++) {
        nextEnd = Math.max(nextEnd, reach[i])

        if (i === currEnd) {
            if (nextEnd <= i) return -1

            cnt++
            currEnd = nextEnd
        }
    }

    return cnt
};