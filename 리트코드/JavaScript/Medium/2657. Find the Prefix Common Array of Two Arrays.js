/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function(A, B) {
    const n = A.length
    const count = Array(n + 1).fill(0)
    const C = Array(n).fill(0)

    for (let i = 0; i < n; i++){
        if (i > 0) C[i] = C[i - 1]

        const a = A[i]
        const b = B[i]

        count[a]++
        count[b]++

        if (a === b) C[i] += 1
        else {
            if (count[a] === 2) C[i]++
            if (count[b] === 2) C[i]++
        }

    }
    return C
};