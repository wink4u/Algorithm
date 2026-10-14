function solution(players, m, k) {
    var answer = 0;
    
    const q = []
    let server = 0
    
    for (let i = 0; i < players.length; i++) {

        while (q.length) {
            const [time, cnt] = q[0]
            
            if (i === time) {
                q.shift()
                server -= cnt
            } else {
                break
            }
        }
        
        const player = players[i]
        
        if (player < m) {
            continue
        } else if (server * m < player) {
            const v =  Math.floor((player - (server * m)) / m)
            server += v
            answer += v
            q.push([i + k, v])
        }
        
    }
    
    return answer;
}
