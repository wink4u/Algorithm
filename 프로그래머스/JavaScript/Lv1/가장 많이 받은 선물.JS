function solution(friends, gifts) {
    var answer = 0;

    var check = {};

    for (let i = 0; i < friends.length; i++) {
        check[friends[i]] = {};
        for (let j = 0; j < friends.length; j++) {
            if (friends[i] !== friends[j]) {
                // 준 선물 받은 선물
                check[friends[i]][friends[j]] = [0, 0];
            } else {
                check[friends[i]][friends[j]] = 0;
            }
        }
    }

    for (let i = 0; i < gifts.length; i++) {
        const [from, to] = gifts[i].split(" ");
        check[from][from] += 1
        check[to][to] -= 1

        check[from][to][0] += 1
        check[to][from][1] += 1
    }

    Object.entries(check).forEach(([name, giftData], index) => {
        res = 0;
        Object.entries(giftData).forEach(([to, giftDatas], index) => {
            if (name !== to){
                const [give, receive] = giftDatas

                if (give > receive) {
                    res += 1
                } else if (give === receive) {
                    if (check[name][name] > check[to][to]) {
                        res += 1
                    }
                }
            }
        })

        answer = Math.max(answer, res);
    })

    return answer;
}