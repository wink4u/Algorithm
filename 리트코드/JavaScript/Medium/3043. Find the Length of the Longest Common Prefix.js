/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var longestCommonPrefix = function(arr1, arr2) {
    const hash = new Set()

    for (let i = 0; i < arr1.length; i++){
        const s = String(arr1[i])
        const m = s.length

        for (let j = 1; j <= m; j++){
            const v = s.slice(0, j)

            if (!hash.has(v)) {
                hash.add(v, true)
            }
        }
    }

    let ans = 0

    for (let i = 0; i < arr2.length; i++){
        const s = String(arr2[i])
        const m = s.length

        for (let j = m; j > 0; j--){
            const v = s.slice(0, j)
            if (hash.has(v)) {
                ans = Math.max(ans, j)
                break
            }
        }
    }

    return ans
};