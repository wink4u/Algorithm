const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)

if (N === 1 || N == 2) {
  console.log(0)
} else {
  const v = []
  
  for (let i = -1; i <= 1; i++){
    const cnt = i !== 0 ? 1 : 0
    for (let j = -1; j <= 1; j++){
      const a = arr[0] + i
      const b = arr[1] + j
      const tmp = j !== 0 ? 1 : 0

      v.push([a - b, b, cnt + tmp])
    }
  }

  let ans = Infinity

  const check = ([diff, prev, cnt]) => {
    for (let i = 2; i < N; i++){
      const now = prev - arr[i]
      if (now - diff === 1) {
        prev = arr[i] + 1
        cnt += 1
      } else if (now - diff === -1) {
        prev = arr[i] - 1
        cnt += 1
      } else if (now - diff === 0) {
        prev = arr[i]
      } else {
        return -1
      }
    }
    return cnt
  }

  for (let i = 0; i < v.length; i++){
    const value = check(v[i])
    if (value !== -1) ans = Math.min(value, ans)
  }
  
  
  console.log(ans === Infinity ? -1 : ans)
}
