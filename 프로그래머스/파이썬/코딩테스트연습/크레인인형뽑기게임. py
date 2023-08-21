def solution(board, moves):
    answer = 0
    
    temp = list()
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] -1]:
                temp.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
 
                if len(temp) > 1:
                    if temp[len(temp) - 1] == temp[len(temp) - 2]:
                        temp.pop()
                        temp.pop()
                        answer += 2
                break
                
 
    return answer