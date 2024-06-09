function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let result = [];
    let bridge = [];
    const LENGTH = truck_weights.length;
    const outTime = bridge_length;

    if (LENGTH === 1) return outTime + 1;

    const status = truck_weights.map(t => {
        return {weight: t, time: 0}
    })

    while(result.length !== LENGTH){
        bridge.forEach(b => {b.time = b.time + 1})
        if(bridge.length === 0) {
            bridge.push(status.shift())
        } else {
            if (status.length === 0){
                if(bridge[0].time === outTime) result.push(bridge.shift())
                answer++;
                continue;
            }

            if (bridge[0].time === outTime) result.push(bridge.shift())
            let sum = bridge.reduce((a, b) => {return a + b.weight}, 0)
            if(weight - sum >= status[0].weight) bridge.push(status.shift())
        }
        answer++;
    }
    return answer;
}