const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number)
const arr = input.slice(1).map((v) => v.split(' ').map(Number))

class minHeap {
    constructor() {
        this.heap = []
    }

    size() {
        return this.heap.length
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    bubbleUp() {
        let index = this.heap.length - 1;
        let parentIndex = Math.floor((index - 1) / 2)

        while (
            this.heap[parentIndex] &&
            this.heap[index][0] < this.heap[parentIndex][0]
        ) {
            this.swap(index, parentIndex)
            index = parentIndex
            parentIndex = Math.floor((index - 1) / 2)
        }
    }

    bubbleDown() {
        let index = 0;
        let leftIdx = index * 2 + 1
        let rightIdx = index * 2 + 2

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

    add(value) {
        this.heap.push(value)
        this.bubbleUp()
    }

    poll() {
        if (this.heap.length === 1) {
            return this.heap.pop()
        }

        const value = this.heap[0];
        this.heap[0] = this.heap.pop()
        this.bubbleDown();
        return value
    }
}

const path = Array(N + 1).fill(0)
const node = Array.from(Array(N + 1), () => [])

arr.forEach((v) => {
    const [a, b, w] = v
    node[a].push([b, w])
    node[b].push([a, w])
})

const djkstra1 = () => {
    const D = Array(N + 1).fill(Infinity)
    D[1] = 0

    const heap = new minHeap();
    heap.add([0, 1])

    while (heap.size()){
        const [dist, now] = heap.poll()

        if (D[now] < dist) continue

        for (let i = 0; i < node[now].length; i++){
            const [nxt, v] = node[now][i]
            const cost = dist + v

            if (D[nxt] > cost) {
                D[nxt] = cost
                path[nxt] = now
                heap.add([cost, nxt])
            }
        }
    }

    const tmp = [N]
    let now = N
    while (true) {
        const nxt = path[now]
        if (nxt === 0) break

        tmp.push(nxt)
        now = nxt
    }
    return [D[N], tmp]
}

const djkstra2 = (ban) => {
    const D = Array(N + 1).fill(Infinity)
    D[1] = 0
    const [a, b] = ban
    const heap = new minHeap();
    heap.add([0, 1])

    while (heap.size()){
        const [dist, now] = heap.poll()

        if (D[now] < dist) continue

        for (let i = 0; i < node[now].length; i++){
            const [nxt, v] = node[now][i]
            if ((now === a && nxt === b) || (now === b && nxt === a)) continue
            
            const cost = dist + v
            if (D[nxt] > cost) {
                D[nxt] = cost
                path[nxt] = now
                heap.add([cost, nxt])
            }
        }
    }

    return D[N]
}


const [v, check] = djkstra1()

let ans = 0;
for (let i = 1; i < check.length; i++){
    const newV = djkstra2([check[i], check[i - 1]])
    if (newV === Infinity) {
        ans = -1
        break
    }

    ans = Math.max(ans, newV - v)
}

console.log(ans)