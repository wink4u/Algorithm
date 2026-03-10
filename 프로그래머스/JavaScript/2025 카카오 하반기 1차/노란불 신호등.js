function solution(signals) {
    var answer = 0;
    const n = signals.length
    const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);
    const lcm = (a, b) => a * b / gcd(a, b);
    const [a, b] = [signals[0].reduce((a, b) => a + b, 0), signals[1].reduce((a, b) => a + b, 0)]
    
    let now = lcm(a, b)
    
    for (let i = 2; i < n; i++){
        const v = signals[i].reduce((a, b) => a + b, 0)
        now = lcm(now, v)
    }
    
    const check = Array.from(Array(n), () => Array(2).fill(0))

    while (true) {
        let count = 0;
        
        for (let i = 0; i < n; i++){
            const color = check[i][0]
            if (color === 1) count++
            
            check[i][1] += 1
            
            if (check[i][1] === signals[i][color]) {
                check[i][0] = (check[i][0] + 1) % 3
                check[i][1] = 0
            }
        }
        
        answer += 1
        if (count === n) break   
        if (answer === now) {
            answer = -1 
            break
        }
        
    }
    return answer;
}