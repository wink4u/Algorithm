function solution(numbers) {
    var answer = new Array(numbers.length).fill(1);
    
    const transBinary = (num) => {
        const tmp = []
        while (num !== 0) {
            const v = num % 2
            num = (num - v) / 2
            tmp.push(v)
        }
        
        let cnt = 1
        
        while (tmp.length >= cnt) {
            cnt *= 2
        }
        
        if (tmp.length !== cnt) {
            tmp.push('0'.repeat((cnt - 1) - tmp.length))
        }
        
        return tmp.reverse().join('')
    }
    
    
    const dfs = (now, s, len) => {
        if (s.length === 1) return
        const idx = Math.floor(len / 2)
        
        if (answer[now]) {
            if (s[idx] === '0' && s.includes('1')) {
                answer[now] = 0
            } else {
                dfs(now, s.slice(0, idx), idx)
                dfs(now, s.slice(idx + 1), idx)
            }
        }
    }
    
    for (let i = 0; i < numbers.length; i++){
        const num = transBinary(numbers[i])
        dfs(i, num, num.length)
    }

    return answer;
}