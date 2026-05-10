/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const n = board.length;
    const m = board[0].length;
    
    const dfs = (x, y, wIdx) => {
        if (wIdx === word.length) return true;
        
        if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] !== word[wIdx]) {
            return false;
        }

        const temp = board[x][y];
        board[x][y] = '#'; 

        const found = dfs(x + 1, y, wIdx + 1) ||
                      dfs(x - 1, y, wIdx + 1) ||
                      dfs(x, y + 1, wIdx + 1) ||
                      dfs(x, y - 1, wIdx + 1);

        board[x][y] = temp;

        return found;
    };

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (board[i][j] === word[0] && dfs(i, j, 0)) {
                return true;
            }
        }
    }

    return false;
};