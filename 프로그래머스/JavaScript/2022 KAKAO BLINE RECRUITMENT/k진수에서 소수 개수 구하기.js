function solution(n, k) {
    var answer = 0;
    
    const arr = []
    
    while (n !== 0) {
        const v = n % k
        arr.push(v)
        n = (n - v) / k
    }
    
    const number = arr.reverse().join('').split('0').map(Number)
    
    const prime = (num) => {
        for (let i = 2; i * i <= num; i++){
            if (num % i === 0) {
                return false
            }
        }
        
        return true
    }
    
    for (let i = 0; i < number.length; i++){
        const v = number[i]
        
        if (v > 1 && prime(v)) answer++
    }
    
    return answer;
}