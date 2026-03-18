const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

let idx = 0
const res = []

while (true) {
    const [n, k] = input[idx++].split(' ').map(Number)

    if (n === 0 && k === 0) break

    const parent = Array(n).fill(-1)
    const child = Array.from(Array(n), () => [])
    const arr = input[idx++].split(' ').map(Number)


    let kIdx = 0
    for (let i = 0; i < n; i++){
        if (arr[i] === k) {
            kIdx = i
            break
        }
    }

    let node = [0]
    let start = 1;
    let flag = 0

    while (true) {
        if (flag) break

        const tmp = []

        for (let i = 0; i < node.length; i++) {
            const now = node[i]

            let before
            const v = []

            while (true) {
                if (start === n) {
                    flag = 1
                    break
                }

                if (!v.length) {
                    before = arr[start]
                } else {
                    if (before + 1 === arr[start]) {
                        before = arr[start]
                    } else {
                        break
                    }
                }

                parent[start] = now
                v.push(start)
                tmp.push(start)
                start++
            }
            
            child[now] = v
        }

        node = tmp
    }

    const mother = parent[kIdx]
    if (mother === -1) {
        res.push('0')
        continue
    }

    const grandmother = parent[mother]

    if (grandmother === -1) {
        res.push('0')
        continue
    }

    const v = child[grandmother]
    let ans = 0

    for (let i = 0; i < v.length; i++){
        if (mother !== v[i]) {
            ans += child[v[i]].length
        }
    }

    res.push(String(ans))
}

console.log(res.join('\n'))