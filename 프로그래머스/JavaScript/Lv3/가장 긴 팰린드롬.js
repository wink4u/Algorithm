function solution(s)
{
    if (s.length === 1) return 1

    var answer = 1;
    for (let i = 0; i <= s.length - 2; i++) {
        const now = s[i]
        const next = s[i + 1]
        const nnext = s[i + 2]

        if (now === next){
            const getParil = check(i, i + 1, s)
            answer = Math.max(getParil, answer)
        }

        if (now === nnext){
            const getParil = check(i, i + 2, s) + 1
            answer = Math.max(answer, getParil)
        }
    }

    return answer;
}

function check(l, r, s) {
    let cnt = 0
    while (l >= 0 && r < s.length && s[l] === s[r]){
        l--
        r++
        cnt++
    }
    return cnt * 2
}