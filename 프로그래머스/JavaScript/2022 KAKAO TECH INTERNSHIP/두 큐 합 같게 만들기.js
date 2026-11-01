class Queue {
  constructor() {
    this.storage = {};
    this.front = 0;
    this.rear = 0;
  }

  enqueue(value) {
    if (this.size() === 0) {
      this.storage['0'] = value;
    } else {
      this.rear += 1;
      this.storage[this.rear] = value;
    }
  }
  
  dequeue() {
    if (this.size() === 0) return undefined;
    const value = this.storage[this.front];
    delete this.storage[this.front];
    
    if (this.front === this.rear) {
      this.front = 0;
      this.rear = 0;
    } else {
      this.front += 1;
    }
    return value;
  }

  size() {
    if (this.storage[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.front + 1;
    }
  }

  isEmpty() {
    return this.size() === 0;
  }

  peek() {
    return this.storage[this.front];
  }
}

function solution(queue1, queue2) {
    var answer = -2;
    
    let aCnt = 0, bCnt = 0
    const aQueue = new Queue()
    const bQueue = new Queue()
    
    let aTotal = 0, bTotal = 0
    
    for (let i = 0; i < queue1.length; i++){
        const av = queue1[i]
        const bv = queue2[i]
        
        aTotal += av
        bTotal += bv
        
        aQueue.enqueue(av)
        bQueue.enqueue(bv)
    }
    
    const sum = aTotal + bTotal
    
    if (sum % 2) return -1
    const isSame = sum / 2
    
    
    
    while (true) {
        if (aTotal === bTotal) {
            return aCnt + bCnt    
        }
        
        if (aTotal > bTotal) {
            const v = aQueue.dequeue()
            bQueue.enqueue(v)
            aCnt++
            aTotal -= v
            bTotal += v
        } else {
            const v = bQueue.dequeue()
            aQueue.enqueue(v)
            bCnt++
            aTotal += v
            bTotal -= v
        }
        
        
        if (aCnt > queue1.length && bCnt > queue2.length) {
            return -1
        }
    }
    
    
    return answer;
}