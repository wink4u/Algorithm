from collections import defaultdict

def solution(input_string):
    answer = []
    check = defaultdict(list)
    n = len(input_string)
    idx = 0

    while idx < n:
        v = input_string[idx]
        cnt = 1

        while idx + 1 < n and input_string[idx] == input_string[idx + 1]:
            cnt += 1
            idx += 1

        check[v].append(cnt)
        idx += 1

    check_item = list(check.items())
    for i in range(len(check_item)):
        key, value = check_item[i]
        set_value = set(value)

        if len(value) >= 2:
            answer.append(key)

    if answer:
        answer.sort()
        return ''.join(answer)
    else:
        return 'N'