const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);


class minHeap {
    constructor() {
        this.heap = []
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    size() {
        return this.heap.length
    }

    bubbleUp() {
        let index = this.heap.length - 1
        let parentIdx = Math.floor((index - 1) / 2)

        while (this.heap[parentIdx] && this.heap[parentIdx][1] > this.heap[index][1]) {
            this.swap(index, parentIdx)
            index = parentIdx
            parentIdx = Math.floor((index - 1) / 2)
        }
    }


    bubbleDown() {
        let index = 0
        let leftIdx = index * 2 + 1
        let rightIdx = index * 2 + 2

        while (
            (this.heap[leftIdx] && this.heap[leftIdx][1] < this.heap[index][1]) ||
            (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[index][1])
        ) {
            let smallIdx = leftIdx

            if (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[leftIdx][1]){
                smallIdx = rightIdx
            }

            this.swap(index, smallIdx)
            index = smallIdx
            leftIdx = index * 2 + 1
            rightIdx = index * 2 + 2
        }
    }

    add(v) {
        this.heap.push(v)
        this.bubbleUp()
    }

    poll() {
        if (this.size() === 1) {
            return this.heap.pop()
        }

        const v = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()
        return v
    }

    present() {
        return this.heap
    }
}

const [N, M, K] = input[0].split(' ').map(Number)
const node = Array.from(Array(N + 1), () => [])

for (const [u, v, w] of input.slice(1).map(v => v.split(' ').map(Number))) {
    node[u].push([v, w])
    node[v].push([u, w])
}

const djkstra = () => {
    const q = new minHeap()
    const D = Array.from(Array(N + 1), () => Array(K + 1).fill(Infinity))

    q.add([1, 0, 0])

    for (let i = 0; i <= K; i++){
        D[1][i] = 0
    }

    while (q.size()) {
        const [now, dist, cnt] = q.poll()

        if (D[now][cnt] < dist) continue

        for (const [nxt, cost] of node[now]){
            const total = dist + cost

            if (D[nxt][cnt] > total) {
                D[nxt][cnt] = total
                q.add([nxt, total, cnt])
            }
            
            if (cnt < K && D[nxt][cnt + 1] > dist) {
                D[nxt][cnt + 1] = dist
                q.add([nxt, dist, cnt + 1])
            }
        }
    }

    let ans = Infinity

    for (let i = 0; i <= K; i++){
        ans = Math.min(ans, D[N][i])
    }

    return ans
}

console.log(djkstra())