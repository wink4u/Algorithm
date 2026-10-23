function solution(fees, records) {
    const carMap = new Map()
    const finalCost = new Map()
    
    const calculator = (ih, im, oh, om) => {
        return om >= im ? (oh - ih) * 60 + (om - im)
                        : ((oh - 1) - ih) * 60 + (60 + om - im)
    }
    
    const costCal = (v) => {
        if (v <= fees[0]) {
            return fees[1]
        } else {
            const mok = (v - fees[0]) / fees[2]
            const rest = (v - fees[0]) % fees[2]
            const money = rest ? Math.floor(mok) + 1 : Math.floor(mok)
            
            return fees[1] + money * fees[3]
        }
    }
    
    
    for (const record of records) {
        const [time, number, status] = record.split(' ')
        const [hour, minute] = time.split(':').map(Number)
        
        
        if (status === 'IN') {
            carMap.set(number, [hour, minute])
            
            if (!finalCost.has(number)) {
                finalCost.set(number, 0)
            }
        } else {
            const [inHour, inMinute] = carMap.get(number)
            
            const v = calculator(inHour, inMinute, hour, minute)
            const t = finalCost.get(number)
            finalCost.set(number, t + v)
            
            carMap.delete(number)
        }
    
    }
    
    for (const [number, [inHour, inMinute]] of carMap.entries()) {
        const v = calculator(inHour, inMinute, 23, 59)
        const t = finalCost.get(number)
        finalCost.set(number, t + v)
        
    } 
    
    const answer = []
    
    for (const [number, time] of finalCost.entries()) {
        const v = costCal(time)
        answer.push([Number(number), v])
    }
    
    answer.sort((a, b) => a[0] - b[0])

    
    return answer.map(v => v[1]);
}