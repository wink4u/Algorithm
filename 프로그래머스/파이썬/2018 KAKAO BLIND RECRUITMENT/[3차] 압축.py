from collections import defaultdict

def solution(msg):
    n = len(msg)
    answer = []
    alpha = defaultdict(int)
    for i in range(65, 91):
        alpha[chr(i)] = i - 64

    if n == 1:
        answer = [alpha[msg]]
    else:
        # 시작 투 포인터
        l, r = 0, 1
        # 딕셔너리에 추가할 번호
        cnt = 27
        while l < r:
            # 현재 now값
            now = alpha[msg[l:r]]
            # 등록이 되있다면
            if now:
                # 한자리 늘리기
                r += 1
                # 늘렸는데 문자의 끝이면 l, r의 문자를 넣음
                if r == n + 1:
                    answer.append(alpha[msg[l:r]])
                    break
            else:
                # 등록이 안되있다면 한 문자를 줄인 알파벳을 answer에 append
                # 문자열 딕셔너리에 추가
                answer.append(alpha[msg[l:r - 1]])
                alpha[msg[l:r]] = cnt
                # 번호 + 1을 하고 left값을 right - 1
                # right값은 left에 + 1
                cnt += 1
                l = r - 1
                r = l + 1

    return answer