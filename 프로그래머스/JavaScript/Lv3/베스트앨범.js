function solution(genres, plays) {
    var answer = [];
    const n = genres.length;
    const songIdx = {};
    const totalCount = {};
    
    for (let i = 0; i < n; i++){
        const genre = genres[i]
        const play = plays[i]
        
        if (totalCount[genre]) totalCount[genre] += play
        else totalCount[genre] = play
        
        if (songIdx[genre]) {
            const [firstPlay, firstIdx] = songIdx[genre][0]
            const [secondPlay, secondIdx] = songIdx[genre][1]
            
            if (firstPlay < play || (firstPlay === play && firstIdx > i)) {
                songIdx[genre][0] = [play, i]
                songIdx[genre][1] = [firstPlay, firstIdx]
            } else if (secondPlay < play || (secondPlay === play && secondIdx > i)) {
                songIdx[genre][1] = [play, i]
            }
        } else {
            songIdx[genre] = [[play, i], [0, 0]]
        }
    }
    
    const countItem = Object.entries(totalCount).sort((a, b) => b[1] - a[1])

    for (let i = 0; i < countItem.length; i++){
        const song = countItem[i][0]
        for (let j = 0; j < 2; j++){
            if (songIdx[song][j][0] > 0) answer.push(songIdx[song][j][1])
        }
    }
    return answer;
}