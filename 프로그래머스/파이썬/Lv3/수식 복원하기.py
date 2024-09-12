_max = 0


def max_num(l, r, c):
    global _max
    _max = max(int(max(l)), int(max(r)), int(max(c)), _max)


def trans(num, target):
    length = len(num)

    n = 0
    for i in range(length):
        n += int(num[i]) * (target ** (length - i - 1))

    return n


def r_trans(num, target):
    res = ''
    if num >= target:
        while num >= target:
            res += str(num % target)
            num = num // target

        res += str(num)

        return res[::-1]
    else:
        return str(num)


def solution(expressions):
    answer = []
    tmp = []

    # 최소 몇진수부터 사용가능한지 max값 설정
    for expression in expressions:
        cal, res = expression.split('=')

        l, c, r = cal.split()
        res = res.strip()

        if res == 'X':
            tmp.append(expression)
            max_num(l, r, '0')
        else:
            max_num(l, r, res)

    # visit배열을 통한 확인가능한 진수 파악
    visit = [False] * 10

    # _max + 1 진수부터 사용가능
    # 왼쪽항과 오른쪽항이 맞는값인지 파악
    # 값이 틀리면 그 진수는 사용못하니 visit[진수] = True 처리
    for expression in expressions:
        if expression not in tmp:
            cal, res = expression.split('=')

            l, c, r = cal.split()
            res = res.strip()

            for i in range(int(_max) + 1, 10):
                if not visit[i]:
                    l_value = trans(l, i)
                    r_value = trans(r, i)
                    res_value = trans(res, i)

                    if c == '+':
                        if l_value + r_value != res_value:
                            visit[i] = True
                    else:
                        if l_value - r_value != res_value:
                            visit[i] = True

    # answer에 넣는값을 이제 파악
    # 사용가능한 최소 진수부터 시작
    # visit[i] = True는 사용못하는 건너띔
    # set()에 다 동일한 값이 나오는지 파악 -> set()의 크기가 1이면
    # 모두 같은값이니 그 값이 정답 아니면 ? 이 정답
    for t in tmp:
        cal, res = t.split('=')
        l, c, r = cal.split()

        right = set()
        flag = 0

        for i in range(int(_max) + 1, 10):
            if not visit[i]:
                l_value = trans(l, i)
                r_value = trans(r, i)

                if c == '+':
                    right.add(r_trans((l_value + r_value), i))
                else:
                    right.add(r_trans((l_value - r_value), i))

        if len(right) > 1:
            answer.append(f'{l} {c} {r} = ?')
        else:
            right = list(right)
            answer.append(f'{l} {c} {r} = {right[0]}')

    return answer