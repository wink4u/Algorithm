function solution(alp, cop, problems) {
    var answer = 0;
    
    // 초깃값 alp,cop 알고력 코딩력
    // 필요한 알고력 코딩력 p0, p1, 증가하는 알고력 코딩력 p2, p3, 시간 p4
    
    let [n, m] = [alp, cop]
    let len = problems.length
    for (let i = 0; i < len; i++){
        n = Math.max(n, problems[i][0])
        m = Math.max(m, problems[i][1])
    }
    
    // n은 알고력 m은 코딩력
    const dp = Array.from(Array(n + 1), () => Array(m + 1).fill(Infinity))
    dp[alp][cop] = 0
    
    for (let i = alp; i <= n; i++){
        for (let j = cop; j <= m; j++){
            if (i + 1 <= n) dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1)
            if (j + 1 <= m) dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1)
            if (i === n && j === m) break;
            
            for (let k = 0; k < len; k++){
                const [pre_al, pre_co, plus_al, plus_co, time] = problems[k]
                
                if (i >= pre_al && j >= pre_co) {
                    const nxt_al = i + plus_al < n ? i + plus_al : n
                    const nxt_co = j + plus_co < m ? j + plus_co : m
                    dp[nxt_al][nxt_co] = dp[nxt_al][nxt_co] < dp[i][j] + time ? dp[nxt_al][nxt_co] : dp[i][j] + time
                }
            }
            
        }
    }
    
    return dp[n][m];
}