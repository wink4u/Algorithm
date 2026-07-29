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

const N = Number(input[0])
const arr = input.slice(1).map(v => v.trim().split(' '))

const node = Array.from(Array(52), () => [])

for (const [u, v, w] of arr){
    let uNum = u.charCodeAt()
    let vNum = v.charCodeAt()

    uNum -= uNum <= 90 ? 65 : 71
    vNum -= vNum <= 90 ? 65 : 71

    node[uNum].push([vNum, Number(w)])
    node[vNum].push([uNum, Number(w)])
}


const djkstra = () => {
    const q = new minHeap()
    const D = Array(52).fill(Infinity)
    D[25] = 0
    
    q.add([25, 0])
    let cow = ''
    let ans = Infinity

    while (q.size()){
        const [now, dist] = q.poll()
        
        if (D[now] < dist) continue
    
        for (const [nxt, cost] of node[now]) {
            const total = dist + cost
    
            if (D[nxt] > total) {
                if (nxt <= 24) {
                    if (ans > total) {
                        ans = total
                        cow = String.fromCharCode(nxt + 65)
                    }

                    continue
                }
                
                D[nxt] = total
                q.add([nxt, total])
            }
        }
    }

    return [cow, ans]
}

console.log(djkstra().join(' '))