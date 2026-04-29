function solution(cost, hint) {
    var answer = Infinity;
    const n = cost.length
    
    const dfs = (stage, total, v) => {
        if (stage === n - 1) {
            answer = Math.min(answer, total + cost[stage][Math.min(v[stage], n - 1)])
            return
        }
        
        if (total > answer) return
        
        // 표 구매
        for (let i = 1; i < hint[stage].length; i++){
            const tmp = hint[stage][i] - 1
            v[tmp]++
        }
        
        dfs(stage + 1, total + hint[stage][0] + cost[stage][Math.min(v[stage], n - 1)], v)
        
        // 표 구매 취소
        for (let i = 1; i < hint[stage].length; i++){
            const tmp = hint[stage][i] - 1
            v[tmp]--
        }
        
        dfs(stage + 1, total + cost[stage][Math.min(v[stage], n - 1)], v)
    }
    
    dfs(0, 0, Array(n).fill(0))
    
    return answer;
}