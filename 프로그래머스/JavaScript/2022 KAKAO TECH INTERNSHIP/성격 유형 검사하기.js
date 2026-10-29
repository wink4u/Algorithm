function solution(survey, choices) {
    var answer = [];
    const n = survey.length
    
    const graph = {'R': 0, 'T': 1, 'C': 2, 'F': 3, 'J': 4, 'M': 5, 'A': 6, 'N': 7}
    const score = new Array(8).fill(0)
    const MBTI = ['RT', 'CF', 'JM', 'AN']
    
    for (let i = 0; i < n; i++){
        const sv = survey[i]
        const choice = choices[i]
        
        if (choice > 4) {
            score[graph[sv[1]]] += choice - 4
        } else if (choice < 4) {
            score[graph[sv[0]]] += 4 - choice
        }
    }
    
    for (let i = 0; i < 8; i += 2) {
        if (score[i] < score[i + 1]) {
            answer.push(MBTI[i / 2][1])
        } else {
            answer.push(MBTI[i / 2][0])
        }
    }
    

    return answer.join('');
}