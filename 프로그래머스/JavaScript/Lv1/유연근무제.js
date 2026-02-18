function solution(schedules, timelogs, startday) {
    var answer = 0;
    
    const n = schedules.length
    
    for (let i = 0; i < n; i++){
        const rest = (schedules[i] % 100) + 10
        let time = 0;
        let now = startday
        
        if (rest >= 60) {
            time = (schedules[i] + 50)    
        } else {
            time = schedules[i] + 10
        }
        
        let flag = 0
        
        for (let j = 0; j < 7; j++) {
            const v = now % 7
            
            if (v !== 6 && v !== 0) {
                if (timelogs[i][j] > time) {
                    flag = 1
                    break
                }
            }
  
            now++
        }
        
        if (!flag) answer++
    }
    return answer;
}