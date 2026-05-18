/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    const hash = new Map()
    const n = arr.length

    for (let i = 0; i < n; i++){
        const num = arr[i]

        if (!hash.has(num)) hash.set(num, [])
        hash.get(num).push(i)
    }

    const q = [0]
    let idx = 0

    const visit = Array(n).fill(0)
    visit[0] = 1

    let ans = 0;
    while (q.length > idx) {
        const size = q.length - idx
        const lastIdx = q.length

        for (let i = idx; i < lastIdx; i++){
            const cur = q[i]
            if (cur === n - 1) return ans

            if (cur + 1 < n && !visit[cur + 1]) {
                visit[cur + 1] = 1
                q.push(cur + 1)
            }

            if (cur - 1 >= 0 && !visit[cur -1]) {
                visit[cur - 1] = 1
                q.push(cur - 1)
            }

            for (const nxt of hash.get(arr[cur])) {
                if (!visit[nxt]) {
                    visit[nxt] = 1
                    q.push(nxt)
                }
            }

            hash.set(arr[cur], [])
        }

        idx += size
        ans++
    }

    return -1
};