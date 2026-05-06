function solution(k, ranges) {
    var answer = [];
    const sum = [0]
    
    let idx = 0
    while (k > 1) {
        const before = k
        if (k % 2) k = k * 3 + 1
        else k /= 2
        
        sum.push(sum[idx++] + (before + k) / 2)
    }
    
    
    function hasDecimal(num) {
        return typeof num === 'number' && num % 1 !== 0;
    }
    
    const n = sum.length - 1
 
    for (let [a, b] of ranges) {
        b += n
        
        if (a > b) answer.push(-1.0)
        else {
            const v = sum[b] - sum[a]
            if(!hasDecimal(v)) answer.push(v.toFixed(1))
            else answer.push(v)
        }
    }
    
    return answer;
}