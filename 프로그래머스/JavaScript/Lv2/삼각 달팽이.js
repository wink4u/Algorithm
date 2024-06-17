function solution(n) {
    var answer = [];
    var arr = [];
    
    for (let i = 1; i < n + 1; i++){
        const tmp = new Array(i).fill(0)
        arr.push(tmp)
    }
    
    const dx = [1, 0, -1]
    const dy = [0, 1, -1]
    
    let dir = 0;
    arr[0][0] = 1
    let [x, y] = [0, 0]
    
    const res = Array(n).fill(1).map((i, idx) => i + idx).reduce((a, b) => a + b)
    
    while (true) {
        const [nx, ny] = [x + dx[dir], y + dy[dir]]
        let flag = 1;
        if (arr[x][y] === res) break;
        
        if (0 <= nx && nx < n && 0 <= ny && ny < arr[nx].length) {
            if(arr[nx][ny] === 0) {
                arr[nx][ny] = arr[x][y] + 1
                x = nx
                y = ny
                
                flag = 0
            } 
        } 
        
        if(flag === 1) {
            dir += 1
            if (dir === 3){
                dir = 0
            }
        }
    }
    
    arr.forEach(([...value]) => {
        answer.push(...value)
    })
    
    return answer;
}