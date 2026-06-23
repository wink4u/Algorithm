const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = input.length
const res = []

for (let i = 0; i < N; i++){
    let flag = 0
    const s = input[i].trim().split(' ').map(Number)
    const arr = Array.from({length : 6}, (_, j) => s.slice(j * 3, j * 3 + 3))

    for (let j = 0; j < 6; j++){
        const v = arr[j].reduce((a, b) => a + b, 0)
        if (v !== 5) {
            flag = 2
            res.push(0)
            break
        }
    }

    if (flag === 2) continue

    const dfs = (idx, nxt) => {
        if (flag) {
            return
        }
        
        if (idx === 5) {
            flag = 1
            return
        }
        
        if (arr[idx][0] && arr[nxt][2]) {
            arr[idx][0]--
            arr[nxt][2]--
            
            if (nxt === 5) dfs(idx + 1, idx + 2)
            else dfs(idx, nxt + 1)
            
            arr[idx][0]++
            arr[nxt][2]++
        }
        
        if (arr[idx][1] && arr[nxt][1]) {
            arr[idx][1]--
            arr[nxt][1]--
            
            if (nxt === 5) dfs(idx + 1, idx + 2)
            else dfs(idx, nxt + 1)
            
            arr[idx][1]++
            arr[nxt][1]++
        }
    
        if (arr[idx][2] && arr[nxt][0]) {
            arr[idx][2]--
            arr[nxt][0]--
            
            if (nxt === 5) dfs(idx + 1, idx + 2)
            else dfs(idx, nxt + 1)
            
            arr[idx][2]++
            arr[nxt][0]++
        }
    }

    dfs(0, 1)
    res.push(flag)

}

console.log(res.join(' '))

