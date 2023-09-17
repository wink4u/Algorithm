from collections import deque

def solution(elements):
    # DP 마지막에 넣을 값
    last = sum(elements)
    
    # start, end로 elements의 인덱스 값을 더할 것을 설정
    start, end = 0, 1
    
    # check라는 변수를 통해 elements의 길이를 저장
    check = len(elements)
    
    # cnt 값은 총 길이의 값 * 길이 -1값을 곱한 만큰 DP작업해야함
    cnt = len(elements) * (len(elements) - 1)
    
    # count_end는 end의 값을 변형해주기 위한 것
    # 각 길이 부분수열을 끝날때마다 end값을 변경해야함
    count_end = 1
    
    # 부분수열 count 변수
    count = 0
    
    # while문은 elements의 길이는 부분수열을 마칠때가 cnt값 이므로
    # 계속 돌려야함
    while len(elements) != cnt:
        # 길이의 부분수열을 마치면
        if count == check:
            # end값을 변경 및 count변수 0으로 초기화
            count_end += 1
            end = count_end
            count = 0
        
        # 부분수열 시작
        result = elements[start] + elements[end]
        elements.append(result)
        
        # start, end 값을 올려 진행
        start += 1
        end += 1
        count += 1
        
        # 만약 end의 값이 elements의 길이만큼 되면 0으로 초기화
        if end == check:
            end = 0
    
    # 전체 더하는 값은 마지막에 진행
    elements.append(last)
    # set으로 중복 값 제거
    temp = set(elements)
        
    return len(temp)