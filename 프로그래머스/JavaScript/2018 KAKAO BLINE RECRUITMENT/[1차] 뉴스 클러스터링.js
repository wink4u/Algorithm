function solution(str1, str2) {
    const changeStr = (v) => {
        return v.toLowerCase().split('').join('')   
    }
    
    const a = changeStr(str1), b = changeStr(str2)
    
    const isAlpha = (s) => {
        const v = s.charCodeAt()
        return v >= 97 && v <= 122
    }
    
    let total = 0
    
    const checkStr = (v) => {
        const n = v.length
        const map = new Map()
        
        for (let i = 0; i < n - 1; i++){
            if (!isAlpha(v[i]) || !isAlpha(v[i + 1])) continue
            
            const s = v[i] + v[i + 1]
            
            map.set(s, map.get(s) + 1 || 1)
            total++
        }
        
        return map
    }
    
    const aMap = checkStr(a)
    const bMap = checkStr(b)
    
    let join = 0
    
    aMap.forEach((aValue, aKey) => {
        if (bMap.get(aKey)) {
            join += Math.min(aValue, bMap.get(aKey))
        }
    })
    
    total -= join

    
    return total === 0 ? 65536 : Math.floor(65536 * (join / total));
}