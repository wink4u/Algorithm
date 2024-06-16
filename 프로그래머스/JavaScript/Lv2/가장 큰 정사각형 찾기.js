function solution(board)
{
    var answer = 0;
    const R = board.length
    const C = board[0].length;
    if (R <= 1 && C <= 1) {
        return 1
    }

    for (let i = 1; i < R; i++){
        for (let j = 0; j < C; j++) {
            if (board[i][j] > 0){
                const up = board[i - 1][j]
                const left = board[i][j - 1]
                const cross = board[i - 1][j - 1]
                if (up > 0 && left > 0 && cross > 0) {
                    board[i][j] = Math.min(up, left, cross) + 1
                }
                answer = Math.max(answer, board[i][j])

            }
        }
    }

    console.log(board)

    return answer ** 2;
}