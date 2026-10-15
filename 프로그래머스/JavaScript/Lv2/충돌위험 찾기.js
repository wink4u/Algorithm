function solution(points, routes) {
    let crush = 0;
    let finish = 0;
    
    // 각 로봇의 번호에 맞은 현재 위치
    const check = [];
    // 로봇들의 마지막 지점
    const end = routes[0].length - 1
    // 로봇의 현재 index
    const robot = new Array(routes.length).fill(0);
    // 완료 로봇
    const finishRobot = new Array(routes.length).fill(0);
    
    const firstMap = new Map()
    
    const checkCrush = (robotMap) => {
        for (const v of robotMap.values()) {
            if (v) {
                crush++
            }
        }
    }
    
    for (let i = 0; i < routes.length; i++){
        const [y, x] = points[routes[i][0] - 1]
        check.push([y, x])
    
        firstMap.set(`${y},${x}`, firstMap.get(`${y},${x}`) + 1 || 0)
    }
    
    checkCrush(firstMap)

    
    const move = () => {
        const moveMap = new Map()
        
        for (let i = 0; i < routes.length; i++){
            if (!finishRobot[i]) {
                const nxtPoint = routes[i][robot[i] + 1]
                
                const [y, x] = check[i]
                const [ny, nx] = points[nxtPoint - 1]
                
                if (ny !== y) {
                    if (ny > y) check[i][0] += 1
                    else check[i][0] -= 1
                } else if (nx !== x) {
                    if (nx > x) check[i][1] += 1
                    else check[i][1] -= 1
                } 
                
                const [cy, cx] = check[i]
                
                if (ny === cy && nx === cx) {
                    robot[i] += 1
                    
                    if (robot[i] === end) {
                        finishRobot[i] = 1
                        finish++
                    }
                }
                
                
                moveMap.set(`${cy},${cx}`, moveMap.get(`${cy},${cx}`) + 1 || 0)
            }
        }
        
        checkCrush(moveMap)
    }
    
    while (finish !== routes.length) {
        move()   
    }
    
    return crush;
}