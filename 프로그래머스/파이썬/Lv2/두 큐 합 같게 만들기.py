from collections import deque

def solution(queue1, queue2):
    one_q = deque(queue1)
    two_q = deque(queue2)

    que1_sum = sum(queue1)
    que2_sum = sum(queue2)

    total = que1_sum + que2_sum

    one_cnt = 0
    two_cnt = 0

    flag = 0

    while True:

        if que1_sum == total // 2 and que2_sum == total // 2:
            break

        if que1_sum > que2_sum:
            one = one_q.popleft()
            two_q.append(one)

            que2_sum += one
            que1_sum -= one

            one_cnt += 1

        else:
            two = two_q.popleft()
            one_q.append(two)

            que1_sum += two
            que2_sum -= two

            two_cnt += 1

        if one_cnt >= len(queue1) and two_cnt >= len(queue2):
            flag = 1
            break

    if flag == 0:
        answer = one_cnt + two_cnt
    else:
        answer = -1

    return answer