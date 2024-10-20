const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];
let t = 1;

function find(a) {
    if (a === parent[a]) {
        return a;
    }
    parent[a] = find(parent[a]);
    return parent[a];
}

function union(a, b) {
    const pa = find(a);
    const pb = find(b);

    if (pa < pb) {
        parent[pb] = pa;
    } else {
        parent[pa] = pb;
    }
}

rl.on("line", function (line) {
    input.push(line.trim());
}).on("close", function () {
    let index = 0;
    
    while (index < input.length) {
        let [n, m] = input[index].split(" ").map(Number);
        index++;

        if (n === 0 && m === 0) {
            break;
        }

        parent = Array.from({ length: n + 1 }, (_, i) => i);
        let cycle = new Set();

        for (let i = 0; i < m; i++) {
            let [a, b] = input[index].split(" ").map(Number);
            index++;

            if (find(a) === find(b)) {
                cycle.add(parent[a]);
            }

            if (cycle.has(parent[a]) || cycle.has(parent[b])) {
                cycle.add(parent[a]);
                cycle.add(parent[b]);
            }

            union(a, b);
        }

        for (let i = 1; i <= n; i++) {
            find(i); // 경로 압축
        }

        let s_parent = Array.from(new Set(parent.slice(1)));
        let treeCount = s_parent.reduce((count, p) => count + (cycle.has(p) ? 0 : 1), 0);

        if (treeCount === 0) {
            console.log(`Case ${t}: No trees.`);
        } else if (treeCount === 1) {
            console.log(`Case ${t}: There is one tree.`);
        } else {
            console.log(`Case ${t}: A forest of ${treeCount} trees.`);
        }
        t++;
    }
    process.exit();
});