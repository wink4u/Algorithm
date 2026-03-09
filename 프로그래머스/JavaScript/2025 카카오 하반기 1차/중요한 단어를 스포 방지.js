function solution(message, spoiler_ranges) {
    const count = {}
    const check = new Set()
    
    const msg = message.split(' ')
    
    const isSpoiler = (start, end, s, e) => {
        return !(end < s || e < start)
    }
    
    let start = 0
    let idx = 0
    
    for (const m of msg) {
        const end = start + m.length - 1
        
        while (idx < spoiler_ranges.length && spoiler_ranges[idx][1] < start) {
            idx++
        }
        
        count[m] = (count[m] || 0) + 1
        
        let tmp = idx
        
        while (tmp < spoiler_ranges.length && spoiler_ranges[tmp][0] <= end) {
            const [s, e] = spoiler_ranges[tmp]
            
            if (isSpoiler(start, end, s, e)) {
                check.add(m)
                count[m] -= 1
                break
            }
            
            tmp++
        }
        
        start = end + 2
    }
    
    let ans = 0
    
    for (const c of check) {
        if (count[c] === 0) ans++
    }
    
    return ans;
}