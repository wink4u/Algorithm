const readline = require('readline');
const { threadId } = require('worker_threads');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    add(value) {
        this.heap.push(value);
        this.bubbleUp();
    }

    bubbleUp() {
        let index = this.heap.length - 1;
        let parentIdx = Math.floor((index - 1) / 2);

        while (
            this.heap[parentIdx] &&
            this.heap[index][0] < this.heap[parentIdx][0]
        ) {
            this.swap(index, parentIdx);
            index = parentIdx;
            parentIdx = Math.floor((index - 1) / 2);
        }
    }

    poll() {
        if (this.heap.length === 1) {
            return this.heap.pop()
        }

        const value = this.heap[0];
        this.heap[0] = this.heap.pop()
        this.bubbleDown();
        return value;
    }

    bubbleDown() {
        let index = 0;
        let leftIdx = index * 2 + 1
        let rightIdx = index * 2 + 2;
    
        while (
            (this.heap[leftIdx] && this.heap[leftIdx][0] < this.heap[index][0]) ||
            (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[index][0])
        ) {
            let smallIdx = leftIdx;
            if (
                this.heap[rightIdx] &&
                this.heap[rightIdx][0] < this.heap[smallIdx][0]
            ) {
                smallIdx = rightIdx
            }

            this.swap(index, smallIdx)
            index = smallIdx
            leftIdx = index * 2 + 1
            rightIdx = index * 2 + 2
        }
    }
}
rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    // M Log N + (N * (N - 1))
    const [N, M] = input[0].split(' ').map(Number)
    const node = Array.from(Array(N + 1), () => [])

    for (let i = 0; i < M; i++){
        const [A, B] = input[i + 1].split(' ').map(Number)
        node[A].push(B)
        node[B].push(A)
    }

    const djkstra = (num) => {
        let D = Array(N + 1).fill(Infinity);
        D[num] = 0
        const q = new MinHeap();
        q.add([0, num])

        while (q.size() > 0) {
            const [dist, now] = q.poll();

            if (dist > D[now]) continue

            for (const nxt of node[now]) {
                if (dist + 1 < D[nxt]) {
                    D[nxt] = dist + 1
                    q.add([dist + 1, nxt])
                }
            }
        }

        return D.slice(1)
    }

    const ans = [[]];

    for (let i = 1; i <= N; i++){
        ans.push(djkstra(i))
    }

    let res = [Infinity, Infinity, Infinity]

    for (let i = 1; i <= N - 1; i++){    
        for (let j = i + 1; j <= N; j++) {
            let cnt = 0;
            for (let k = 0; k < N; k++){
                cnt += Math.min(ans[i][k], ans[j][k])
            }

            cnt *= 2
            if (cnt < res[2]){
                res = [i, j, cnt]
            } else if(cnt === res[2]) {
                if (res[0] > i) {
                    res[0] = i
                    res[1] = j
                }
            }
        }
    }

    console.log(res.join(' '))

    process.exit();
})
