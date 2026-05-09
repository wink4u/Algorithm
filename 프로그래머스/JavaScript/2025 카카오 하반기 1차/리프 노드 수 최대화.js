function solution(dist_limit, split_limit) {
    var answer = 1;
    
    const dfs = (cur, split, multi, leaf, dLimit, sLimit) => {
        if (split > dLimit) return
        
        answer = Math.max(answer, leaf + cur)
        
        for (let i = 2; i <= 3; i++){
             const v = multi * i
             
             if (v > sLimit) continue
            
            const next = cur * i
            const remain = dLimit - split
            const nextCur = Math.min(next, remain)
            const nextLeaf = leaf + (next - nextCur)
            
            dfs(nextCur, split + nextCur, v, nextLeaf, dLimit, sLimit)
        }
    }
    
    dfs(1, 1, 1, 0, dist_limit, split_limit)
    
    return answer;
}