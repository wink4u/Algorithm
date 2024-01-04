from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    # 입차하는 차들을 담은 dictionay
    cars = defaultdict(int)
    # 출차하고 나오는 값을 담은 dictionary
    result = defaultdict(int)
    
    for record in records:
        time, car, state = record.split()
        
        hour, minute = time.split(':')
        
        if state == 'IN':
            # 입차 계산
            cars[car] = int(hour) * 60 + int(minute)       
        else:
            # 출차 계산
            total = (int(hour) * 60 + int(minute)) - cars.get(car)
            # 같은 차가 계속 들어올 수 도 있기에
            # += 으로 처리를 해줘야함
            result[car] += total
            # 출차가 완료되면 dictionary에서 삭제
            del cars[car]
    
    # 입차하였지만 출차되지 않은 차들을 확인
    if cars:
        for i in cars.items():
            car, time = i
            time = (23 * 60 + 59) - time
            # 기준에 맞춰 계산후 출차
            result[car] += time
    
    # key값으로 오른차순으로 나타내어 answer에 append시키는 작업
    for car, time in sorted(result.items(), key = lambda x : x[0]):
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((time - fees[0])/fees[2]) * fees[3]))
    
    return answer
