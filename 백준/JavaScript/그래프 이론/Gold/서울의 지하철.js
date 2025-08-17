const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const N = Number(input.shift())
    const end = Number(input.pop())

    const subway = {}
    const check = [];

    for (let i = 0; i < N; i++){
        const line = input[i].split(' ').map(Number)
        const K = line[0];
        check.push(line.slice(1))

        for (let j = 1; j <= K; j++) {
            if (subway[line[j]]) subway[line[j]].push(i);
            else subway[line[j]] = [i];
        }
    }

    let min = Infinity;
    subway[0].forEach((v) => {
        const q = [];
        let visit = new Set();

        q.push([0, 0, v])
        visit.add(0);

        while (q.length > 0){
            const [now, cnt, subLine] = q.shift();

            if (now === end) {
                min = Math.min(min, cnt)
                break
            }
            subway[now].forEach((line) => {
                const nxtLine = check[line];

                for (let i = 1; i < nxtLine.length; i++){
                    const vv = nxtLine[i];

                    if (visit.has(vv)) continue;
                    visit.add(vv)

                    if (line !== subLine) {
                        q.push([vv, cnt + 1, line])
                    } else {
                        q.push([vv, cnt, line])
                    }
                }
            })
            
        }
    })

    console.log(min === Infinity ? -1 : min)

    process.exit();
})
