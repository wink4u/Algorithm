const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, K1, K2] = input[0].split(' ').map(Number)
const arr = input.slice(1).map((v, i) => v.split(' ').map(Number).concat(i))

// 두 학생 같은 학교, 거리가 K1이하
// 두 학생 다른 학교, 거리가 K2이하

const count = Array(N).fill(0);

const solve = () => {
    // --------------------------------------------------------
    // 1. [같은 학교] 거리가 K1 이하인 친구 수 구하기
    // --------------------------------------------------------
    const sameSchoolCount = new Map();
    let L = 0;

    for (let R = 0; R < N; R++) {
        const [Xr, Sr, rIdx] = arr[R];

        // 윈도우에 R 학생 추가
        sameSchoolCount.set(Sr, (sameSchoolCount.get(Sr) || 0) + 1);

        // 거리가 K1 초과 시 L 포인터 축소 (L은 계속 전진만 함)
        while (Xr - arr[L][0] > K1) {
            const Sl = arr[L][1];
            sameSchoolCount.set(Sl, sameSchoolCount.get(Sl) - 1);
            L++;
        }

        // 현재 R 학생과 같은 학교인 친구 수 (자기 자신 제외 -1)
        count[rIdx] += (sameSchoolCount.get(Sr) - 1);
    }

    // --------------------------------------------------------
    // 2. [다른 학교] 거리가 K2 이하인 친구 수 구하기
    // --------------------------------------------------------
    const diffSchoolCount = new Map();
    L = 0;
    let totalInWindow = 0;

    for (let R = 0; R < N; R++) {
        const [Xr, Sr, rIdx] = arr[R];

        // 윈도우에 R 학생 추가
        diffSchoolCount.set(Sr, (diffSchoolCount.get(Sr) || 0) + 1);
        totalInWindow++;

        // 거리가 K2 초과 시 L 포인터 축소
        while (Xr - arr[L][0] > K2) {
            const Sl = arr[L][1];
            diffSchoolCount.set(Sl, diffSchoolCount.get(Sl) - 1);
            totalInWindow--;
            L++;
        }

        // 다른 학교 친구 수 = (구간 내 전체 인원 - 내 학교 인원)
        const mySchoolInWindow = diffSchoolCount.get(Sr);
        count[rIdx] += (totalInWindow - mySchoolInWindow);
    }
};

solve();

// Output
console.log(count.join(' '));