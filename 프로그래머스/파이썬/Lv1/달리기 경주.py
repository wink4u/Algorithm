from collections import defaultdict

def solution(players, callings):
    sequence = defaultdict(int)
    
    for i in range(len(players)):
        sequence[players[i]] = i
    
    for i in range(len(callings)):
        index = sequence[callings[i]]
        sequence[callings[i]] -= 1
        sequence[players[index - 1]] += 1
        players[index], players[index - 1] = players[index - 1], players[index]
        
    return players