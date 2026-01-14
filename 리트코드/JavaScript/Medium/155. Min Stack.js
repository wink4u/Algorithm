
var MinStack = function() {
    this.stack = []
    this.minStack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    if (this.stack.length > 0) {
        const v = this.getMin()

        if (v >= val) this.minStack.push(val)
    } else {
        this.minStack.push(val)
    }

    this.stack.push(val)

};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    const v = this.getMin()
    const stackPop = this.stack.pop()

    if (v === stackPop) this.minStack.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    const len = this.stack.length
    if (len) return this.stack[len - 1]

    return null
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    const len = this.minStack.length

    if (len) return this.minStack[len - 1]

    return null
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */