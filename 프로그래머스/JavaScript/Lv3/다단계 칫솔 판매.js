function solution(enroll, referral, seller, amount) {
    var answer = [];
    var dict = {};

    const member = enroll.length;

    let cnt = 0;
    for (let i = 0; i < member; i++){
        dict[enroll[i]] = cnt
        cnt += 1
    }

    const tree = Array(member).fill(-1);
    const value = Array(member).fill(0);

    for (let i = 0; i < member; i++) {
        const v = referral[i];

        if (v !== "-"){
            tree[i] = dict[v]
        }
    }

    const dfs = ((child, v) => {
        const parent = tree[child];
        let a = Math.floor(v * 10 / 100)
        let b = v - a;

        if (parent !== -1) {
            if (v * 10 / 100 < 1) {
                value[child] += v
            } else {
                value[child] += b
                dfs(parent, a)
            }
        } else {
            if (v * 10 / 100 < 1) {
                value[child] += v
            } else {
                value[child] += b
            }
        }
    })

    for (let i = 0; i < seller.length; i++){
        const [who, s] = [dict[seller[i]], amount[i] * 100];
        dfs(who, s)
    }

    return value;
}