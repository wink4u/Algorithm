function solution(maze) {
    var answer = Infinity;
    
    const [N, M] = [maze.length, maze[0].length]
    let redSx = 0, redSy = 0, redEx = 0, redEy = 0
    let blueSx = 0, blueSy = 0, blueEx = 0, blueEy = 0
    
    for (let i = 0; i < N; i++){
        for (let j = 0; j < M; j++){
            if (maze[i][j] === 1) {
                redSx = i, redSy = j
            } else if (maze[i][j] === 2) {
                blueSx = i, blueSy = j
            } else if (maze[i][j] === 3) {
                redEx = i, redEy = j
            } else if (maze[i][j] === 4) {
                blueEx = i, blueEy = j
            }
        }
    }
    
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    
    const isMove = (x, y) => {
        return 0 <= x && x < N && 0 <= y && y < M
    }
    
    const redVisit = Array.from(Array(N), () => Array(M).fill(0))
    const blueVisit = Array.from(Array(N), () => Array(M).fill(0))
    
    redVisit[redSx][redSy] = 1
    blueVisit[blueSx][blueSy] = 1
    
    const check = (rx, ry, bx, by, rVisit, bVisit, cnt) => {
        if (rx === redEx && ry === redEy && bx === blueEx && by === blueEy) {
            answer = Math.min(answer, cnt)
            return
        }
        
        if (rx === redEx && ry === redEy) {
            for (let d = 0; d < 4; d++){
                const [nbx, nby] = [bx + dx[d], by + dy[d]]

                if (!isMove(nbx, nby)) continue
                if (maze[nbx][nby] === 5) continue
                if (nbx === rx && nby === ry) continue
                if (bVisit[nbx][nby]) continue
                
                bVisit[nbx][nby] = 1
                check(rx, ry, nbx, nby, rVisit, bVisit, cnt + 1)
                bVisit[nbx][nby] = 0
            }
        } else if (bx === blueEx && by === blueEy) {
            for (let d = 0; d < 4; d++){
                const [nrx, nry] = [rx + dx[d], ry + dy[d]]

                if (!isMove(nrx, nry)) continue
                if (maze[nrx][nry] === 5) continue
                if (nrx === bx && nry === by) continue
                if (rVisit[nrx][nry]) continue
                
                rVisit[nrx][nry] = 1
                check(nrx, nry, bx, by, rVisit, bVisit, cnt + 1)
                rVisit[nrx][nry] = 0
            }
        } else {
            for (let i = 0; i < 4; i++){
                const [nrx, nry] = [rx + dx[i], ry + dy[i]]

                if (isMove(nrx, nry) && !rVisit[nrx][nry]) {

                    if (maze[nrx][nry] === 5) continue

                    for (let j = 0; j < 4; j++){
                        const [nbx, nby] = [bx + dx[j], by + dy[j]]

                        if (isMove(nbx, nby) && !bVisit[nbx][nby]) {
                            if (rx === nbx && ry === nby && bx === nrx && by === nry) {
                                continue
                            }

                            if (nrx === nbx && nry === nby) continue

                            if (maze[nbx][nby] === 5) continue

                            rVisit[nrx][nry] = 1
                            bVisit[nbx][nby] = 1

                            check(nrx, nry, nbx, nby, rVisit, bVisit, cnt + 1)

                            rVisit[nrx][nry] = 0
                            bVisit[nbx][nby] = 0
                        }
                    }
                }
            }
        }
        
    }
    
    check(redSx, redSy, blueSx, blueSy, redVisit, blueVisit, 0)
    
    return answer === Infinity ? 0 : answer;
}