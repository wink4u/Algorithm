/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    const n = matrix.length
    const tmp = matrix.map(row => [...row]);

    console.log(tmp)

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            matrix[c][n - 1 - r] = tmp[r][c];
        }
    }

    return matrix

};