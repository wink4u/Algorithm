const [N, Q] = input[0].split(" ").map(Number);

const check = Array.from({ length: N + 1 }, () => new Set());

for (let i = 1; i <= N; i++) {
    const v = input[i].split(" ").map(Number);
    check[i] = new Set(v.slice(1));
}

const setCheck = (a, b) => {
    if (check[a].size < check[b].size) {
        const tmp = check[a];
        check[a] = check[b];
        check[b] = tmp;
    }

    for (const v of check[b]) {
        check[a].add(v);
    }

    check[b].clear();
};

const out = [];

for (let i = N + 1; i <= N + Q; i++) {
    const [c, ...a] = input[i].split(" ").map(Number);

    if (c === 1) {
        setCheck(a[0], a[1]);
    } else {
        out.push(String(check[a[0]].size));
    }
}

console.log(out.join("\n"));