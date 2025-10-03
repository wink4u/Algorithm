function solution(today, terms, privacies) {
    var answer = [];
    
    const date = today.split('.').map(Number)
    const endValue = {}
    for (const term of terms) {
        const [v, num] = term.split(' ')
        endValue[v] = Number(num)
    }
    

    privacies.forEach((privaice, idx) => {
        const [pDate, v] = privaice.split(' ')
        let [year, month, day] = pDate.split('.').map(Number)
        
        endMonth = endValue[v]
        const plusYear = Math.floor(endMonth / 12), plusMonth = Math.floor(endMonth % 12)
        if (plusYear) year += plusYear
        if (plusMonth) {
            month += plusMonth
            if (month > 12) {
                year += 1
                month %= 12
            }
        }

        if (year < date[0]){
            answer.push(idx + 1)
        } else if (year === date[0]) {
            if (month < date[1]) {
                answer.push(idx + 1)
            } else if (month === date[1]) {
                if (day <= date[2]) answer.push(idx + 1)
            }
        }
    })
    return answer;
}