const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const G = input[1].split(' ').map(Number)
const R = input.slice(2, 2 + N).map((v) => v.split(' ').map(Number))
const mafia = Number(input[N + 2])
const tmp = Array(N).fill(1)
let ans = 0

const dfs = (left, dead, state, day) => {
    if (left === 1 || dead[mafia] == 0) {
        ans = Math.max(ans, day)
        return
    }
    const flag = left % 2 === 0 ? 1 : 0

    // 밤 일때
    if (flag) {
        for (let i = 0; i < N; i++){
            if (!dead[i]) continue;   // 이미 죽은 사람
            if (i === mafia) continue; // 마피아 자신은 못 죽임

            const stateTmp = [...state];

            // i를 죽였을 때 유죄 지수 변화
            for (let j = 0; j < N; j++) {
                if (!dead[j] || i === j) continue;
                stateTmp[j] += R[i][j];
            }

            dead[i] = 0;
            dfs(left - 1, dead, stateTmp, day + 1); // 밤 1회 증가
            dead[i] = 1;
        }
    } else {
        // 낮일 때
        let [max, nxt] = [-Infinity, 0]

        for (let i = 0; i < N; i++){
            if (dead[i]) {
                if (max < state[i]) {
                    max = state[i]
                    nxt = i
                }
            }
        }

        dead[nxt] = 0
        dfs(left - 1, dead, state, day)
        dead[nxt] = 1
    }
}

dfs(N, tmp, G, 0)

console.log(ans)