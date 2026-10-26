function solution(users, emoticons) {
    var answer = [0, 0];
    const n = users.length
    const m = emoticons.length
    
    const discount = (arr) => {
        if (arr.length === m) {
            check(arr)
            return
        }
        
        for (let i = 40; i >= 10; i -= 10) {
            arr.push(i)
            discount(arr)
            arr.pop()
        }
    }
    
    discount([])
    
    function check (arr) {
        const price = new Array(n).fill(0)
        let person = 0;
        let total = 0;
        
        for (let i = 0; i < m; i++){
            const discount = arr[i]
            
            for (let j = 0; j < n; j++){
                const [userDiscount, userCost] = users[j]
                
                if (price[j] >= userCost) continue
                
                if (discount >= userDiscount) {
                    const v =  emoticons[i] * ((100 - discount) / 100)
                    
                    if (price[j] + v >= userCost) {
                        total -= price[j]
                        person++
                        
                        price[j] = userCost
                    } else {
                        total += v
                        price[j] += v
                    }
                }
            }
        }
        
        if (answer[0] < person) {
            answer = [person, total]
        } else if (answer[0] === person && answer[1] < total) {
            answer = [person, total]
        }
        
    }
    
    return answer;
}