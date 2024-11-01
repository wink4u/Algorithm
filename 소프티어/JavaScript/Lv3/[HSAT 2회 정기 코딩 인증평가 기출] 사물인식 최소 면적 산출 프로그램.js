const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.split(' ').map(Number))
}).on('close', function(){
    const [N, K] = input[0];
    const arr = input.slice(1)
    const color = Array.from(Array(K + 1), () => [])
    let min_area = 2000 * 2000

    for (let i = 0; i < arr.length; i++){
        const [x, y, c] = arr[i];
        color[c].push([x, y])
    }

    const dfs = (min_x, max_x, min_y, max_y, num) => {
        if (num == K + 1){
            min_area = Math.min(min_area, (max_x - min_x) * (max_y - min_y))
            return
        }

        for (let i = 0; i < color[num].length; i++){
            const [x, y] = color[num][i]

            const [mx, hx] = [Math.min(min_x, x), Math.max(max_x, x)]
            const [my, hy] = [Math.min(min_y, y), Math.max(max_y, y)]

            if (min_area > (hx - mx) * (hy - my)){
                dfs(mx, hx, my, hy, num + 1)
            }
        }
    }
    dfs(1000, -1000, 1000, -1000, 1)
    console.log(min_area)
})