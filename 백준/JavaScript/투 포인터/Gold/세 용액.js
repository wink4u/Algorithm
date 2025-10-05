const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => input.push(line.trim())).on("close", () => {
    const N = Number(input.shift())
    const arr = input[0].split(' ').map(Number)
    let min = -Infinity
    let ans = [0, 0, 0]

    arr.sort((a, b) => a - b)
    for (let i = 0; i < N; i++){
      const v = arr[i]
      let [left, right] = [i + 1, N - 1]

      while (left < right) {
          const sum = arr[left] + arr[right]
          if (Math.abs(sum + v) < Math.abs(min)) {
              min = sum + v
              ans = [arr[left], arr[right], v]
          }

          if (sum + v === 0){
            break
          } else {
            if (sum + v > 0) {
              right -= 1
            } else {
              left += 1
            }
          }
      }
    }

    ans.sort((a, b) => a - b)
    console.log(ans.join(' '))

});
