/**
 * @param {string} moves
 * @return {number}
 */
var furthestDistanceFromOrigin = function(moves) {
    let left = 0, right = 0, cnt = 0;

    for (let i = 0; i < moves.length; i++){
        const v = moves[i]
        if (v === 'R') right++
        else if (v === 'L') left++
        else cnt++
    }

    return Math.abs(left - right) + cnt
};