function solution(m, n, puddles) {
    const DP = Array.from(Array(n + 1), () => Array(m + 1).fill(0))
    
    DP[1][1] = 1
    const check = {}
    
    for (const [x, y] of puddles) check[`${y},${x}`] = true;
    
    for (let i = 1; i < n + 1; i++){
        for (let j = 1; j < m + 1; j++){
            const v = `${i},${j}`
            if (check[v]) continue
            
            const left = check[`${i},${j - 1}`] === true ? 0 : DP[i][j - 1]
            const up = check[`${i - 1},${j}`] === true ? 0 : DP[i - 1][j]
            
            DP[i][j] += (up + left) % 1000000007
        }
    }
    

    return DP[n][m];
}