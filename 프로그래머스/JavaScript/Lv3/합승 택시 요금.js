function solution(n, s, a, b, fares) {
    var answer = 0;
    var dist = Array.from(Array(n), () => Array(n).fill(1e12));

    fares.forEach((node) => {
        dist[node[0] - 1][node[1] - 1] = node[2]
        dist[node[1] - 1][node[0] - 1] = node[2]
    })

    for (let k = 0; k < n; k++){
        for (let i = 0; i < n; i++){
            for (let j = 0; j < n; j++) {
                if (dist[i][j] > dist[i][k] + dist[k][j]){
                    dist[i][j] = dist[i][k] + dist[k][j]
                }
            }
        }
    }

    for (let i = 0; i < n; i++){
        dist[i][i] = 0
    }

    answer = dist[s - 1][a - 1] + dist[s - 1][b - 1]

    for (let i = 0; i < n; i++){
        if (dist[s - 1][i] !== 1e12 && dist[i][a - 1] !== 1e12 && dist[i][b - 1] !== 1e12){
            answer = Math.min(answer, dist[s - 1][i] + dist[i][a - 1] + dist[i][b - 1])
        }
    }
    return answer;
}