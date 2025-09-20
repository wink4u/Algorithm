const { Console } = require('console');
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

class Heap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length;
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    add(value) {
        this.heap.push(value);
        this.bubbleUp();
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

    bubbleUp() {
        let index = this.heap.length - 1;
        let parentIdx = Math.floor((index - 1) / 2);
        while (
            this.heap[parentIdx] &&
            this.heap[index] < this.heap[parentIdx]
        ) {
            this.swap(index, parentIdx)
            index = parentIdx
            parentIdx = Math.floor((index - 1) / 2)
        }
    }

    bubbleDown() {
        let index = 0;
        let leftIdx = index * 2 + 1;
        let rightIdx = index * 2 + 2;
    
        while (
            (this.heap[leftIdx] && this.heap[leftIdx] < this.heap[index]) ||
            (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[index])
        ) {
            let smallIdx = leftIdx;
            if (
                this.heap[rightIdx] &&
                this.heap[rightIdx] < this.heap[smallIdx]
            ) {
                smallIdx = rightIdx;
            }

            this.swap(index, smallIdx);
            index = smallIdx
            leftIdx = index * 2 + 1;
            rightIdx = index * 2 + 2;
        }
        
    }
}

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const [N, M, K] = input.shift().split(' ').map(Number)
    const heap = new Heap();

    input.forEach((v) => {
        heap.add(-Number(v))
    })

    let cnt = 0;
    let ans = [];
    let check = 0;

    while (true) {
        const value = -heap.poll()
        if (value <= K) break

        check = Math.floor(check / 2) + value
        ans.push(check)
        cnt += 1
        heap.add(-(value - M))

    }

    console.log(cnt)
    console.log(ans.join('\n'))
})