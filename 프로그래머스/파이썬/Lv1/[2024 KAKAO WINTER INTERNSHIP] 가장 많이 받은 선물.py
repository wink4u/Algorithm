def solution(friends, gifts):
    # 친구들의 수
    people = len(friends)
    # 선물을 받을 사람의 선물 갯수 리스트
    answer = [0 for _ in range(people)]
    
    # 선물을 주고 받은 현황 표
    table = [[0 for _ in range(people)] for _ in range(people)]
    # 선물지수 표
    total = [[0 for _ in range(2)] for _ in range(people)]
    
    # gift에 따른 분배
    for gift in gifts:
        A, B = gift.split()
        
        send = friends.index(A)
        take = friends.index(B)
        table[send][take] += 1
        
        total[send][0] += 1
        total[take][1] += 1
        
    for i in range(people - 1):
        for j in range(i + 1, people):
            # 선물을 주고 받은지 확인          
            if table[i][j] > table[j][i]:
                answer[i] += 1
            elif table[i][j] < table[j][i]:
                answer[j] += 1
            else:
                # 선물개수가 같거나 주고 받지 않았다면 지수를 확인
                first = total[i][0] - total[i][1]
                second = total[j][0] - total[j][1]

                if first > second:
                    answer[i] += 1
                elif first < second:
                    answer[j] += 1

    return max(answer)