const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [x, y] = input[0].split(' ').map(Number)
let [xe, ye, dx, dy] = input[1].split(' ').map(Number)
const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);

if (dx === 0) {
    dy = dy > 0 ? 1 : -1
} else if (dy === 0) {
    dx = dx > 0 ? 1 : -1
} else {
    const v = gcd(Math.abs(dx), Math.abs(dy))
    dx /= v
    dy /= v
}

let check = Infinity
let ax = xe, ay = ye

while (true) {
    const dist = Math.sqrt(Math.abs(x - xe) ** 2 + Math.abs(y - ye) ** 2)

    if (dist < check) {
        check = dist
        ax = xe, ay = ye
    } else {
        break
    }

    xe += dx
    ye += dy
}

console.log(ax, ay)