const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])

class MinHeap {
    constructor() {
        this.heap = [];
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    size() {
        return this.heap.length;
    }

    add(value) {
        this.heap.push(value)
        this.bubbleUp()
    }

    poll() {
        if (this.heap.length === 1) {
            return this.heap.pop()
        }

        const value = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()
        return value
    }

    bubbleUp() {
        let index = this.heap.length - 1
        let parentIdx = Math.floor((index - 1) / 2)

        while (
            this.heap[parentIdx] &&
            this.heap[parentIdx] > this.heap[index]
        ) {
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
            (this.heap[leftIdx] && this.heap[leftIdx] < this.heap[index]) ||
            (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[index])
        ) {
            let smallIdx = leftIdx

            if (
                this.heap[rightIdx] && this.heap[rightIdx] < this.heap[leftIdx]
            ) {
                smallIdx = rightIdx
            }

            this.swap(smallIdx, index)
            index = smallIdx
            leftIdx = index * 2 + 1
            rightIdx = index * 2 + 2
        }
    }

    peek() {
        return this.heap[0]
    }

}

const small = new MinHeap()
const large = new MinHeap()
const out = []

const push = (x) => {
    if (x <= -small.peek()) small.add(-x)
    else large.add(x)
}

small.add(-Number(input[1]))
out.push(-small.peek())

for (let i = 2; i <= (N - 1) / 2 + 1; i++) {
    const num = input[i].split(' ').map(Number)
    push(num[0])
    push(num[1])

    while (small.size() > large.size() + 1) large.add(-small.poll())
    while (large.size() > small.size()) small.add(-large.poll())

    out.push(-small.peek())
}

console.log(out.join('\n'))