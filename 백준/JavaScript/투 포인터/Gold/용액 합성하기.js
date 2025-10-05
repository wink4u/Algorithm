const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => input.push(line.trim())).on("close", () => {
  const N = Number(input.shift())
  const arr = input[0].split(' ').map(Number)

  let min = Infinity

  let [left, right] = [0, N - 1]

  while (left < right) {
    const sum = arr[left] + arr[right]
    min = Math.abs(sum) < Math.abs(min) ? sum : min

    if (sum === 0) break
    else if (sum > 0) right -= 1
    else left += 1
  }

  console.log(min)
});
