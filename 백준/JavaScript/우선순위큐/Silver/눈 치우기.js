const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)
let ans = 0

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

}

const heap = new MinHeap()

for (let i = 0; i < N; i++){
    heap.add(-arr[i])
}

while (heap.size()) {

    if (heap.size() === 1) {
        let v = heap.poll()
        v += 1

        if (v !== 0) heap.add(v)
    } else {
        let first = heap.poll()
        let second = heap.poll()

        first += 1
        second += 1

        if (first !== 0) heap.add(first)
        if (second !== 0) heap.add(second)
    }
    ans++

}

console.log(ans > 1440 ? -1 : ans)