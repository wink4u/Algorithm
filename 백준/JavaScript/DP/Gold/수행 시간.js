const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))
const DP = Array(N).fill(0)

const check = {}
let max = 0

for (let i = 0; i < N; i++){
    const [grade, time] = arr[i]
    if (grade === 1) {
        DP[i] = time            
    } 

    if (!check[grade]) check[grade] = [[i, time]]
    else check[grade].push([i, time])

    max = Math.max(max, grade)
}

for (let i = 2; i <= max; i++){
    const node = check[String(i)]

    for (let j = 0; j < node.length; j++){
        const [idx, time] = node[j]
        const prevNode = check[String(i - 1)]

        for (let k = 0; k < prevNode.length; k++){
            const [prevIdx, _] = prevNode[k]

            DP[idx] = Math.max(DP[idx], DP[prevIdx] + (idx - prevIdx) ** 2)
        }

        DP[idx] += time
    }
}

console.log(Math.max(...DP))