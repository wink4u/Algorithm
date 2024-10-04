def solution(k, n, reqs):
    member = [[] for _ in range(k + 1)]
    arr = []

    for i in range(len(reqs)):
        member[reqs[i][2]].append(reqs[i])

    # n개의 수만큼 k의 유형을 나눠야함
    def make_num(tmp):
        if len(tmp) == k + 1:
            if sum(tmp) == n:
                arr.append(tmp[:])
            return

        if sum(tmp) > n:
            return

        for i in range(1, n - k + 2):
            tmp.append(i)
            make_num(tmp)
            tmp.pop()

    make_num([0])
    _min = 1e10

    for i in range(len(arr)):
        answer = 0
        count = 0

        for j in range(1, k + 1):
            num = arr[i][j]
            count += 1
            min_flag = 0

            if member[j]:
                flag = [0] * num

                for t in range(len(member[j])):
                    flag.sort()
                    s, e, _ = member[j][t]
                    if flag[0]:
                        if flag[0] > s:
                            answer += flag[0] - s
                            flag[0] += e
                        else:
                            flag[0] = s + e
                    else:
                        flag[0] = s + e

                    if _min < answer:
                        min_flag = 1
                        break

            if min_flag:
                break
            if count == k:
                _min = min(_min, answer)
    print(_min)
    return _min