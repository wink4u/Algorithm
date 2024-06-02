function solution(cards1, cards2, goal) {
    var answer = '';
    let [idx1, idx2] = [0, 0]

    for (let i = 0; i < goal.length; i++) {
        const now = goal[i];

        if (cards1[idx1] === now) {
            idx1 += 1
        } else if (cards2[idx2] === now) {
            idx2 += 1
        } else {
            return "No"
        }
    }
    return "Yes";
}