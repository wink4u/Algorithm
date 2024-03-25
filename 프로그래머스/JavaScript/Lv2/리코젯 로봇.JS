function solution(board) {
    var answer = 0;
    board = board.map(i => i.split(''));

    const [N, M] = [board.length, board[0].length];
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1 ,1];
    const q = [];
    for (let i = 0; i < N; i++){
        let flag = 0;
        for (let j = 0; j < M; j++){
            if (board[i][j] === 'R'){
                q.push([i, j]);
                board[i][j] = 'O';
                flag = 1;
            }
        }
        if (flag)
            break;
    }

    while (q.length) {
        const size = q.length;

        for (let i = 0; i < size; i++){
            const [x, y] = q.shift();

            for (let d = 0; d < 4; d++){
                let nx = x + dx[d];
                let ny = y + dy[d];

                while (nx >= 0 && nx < N && ny >= 0 && ny < M && board[nx][ny] !== 'D'){
                    nx += dx[d];
                    ny += dy[d];
                }

                nx -= dx[d];
                ny -= dy[d];

                if (board[nx][ny] === 'G')
                    return answer + 1;

                if (board[nx][ny] !== 'O'){
                    board[nx][ny] = 'O';
                    q.push([nx, ny])
                }
            }
        }
        answer++;
    }

    return -1;
}