def solution(users, emoticons):
    answer = []

    # 서비스 가입자를 최대한 늘림
    # 그리고 판매액을 최대한 늘림

    # n명의 카카오톡 사용자들에게 이모티콘 m개를 할인해서 판매
    # 할인율을 다 다르고, 10% ~ 40% 중 하나로 설정

    discount = [10, 20, 30, 40]

    res = []

    def check(value):
        res_man, res_money = 0, 0
        for i in range(len(users)):
            per, money = users[i]
            check_money = 0
            flag = 0
            for j in range(len(value)):
                if per <= value[j][1]:
                    if money > value[j][0]:
                        money -= value[j][0]
                        check_money += value[j][0]
                    else:
                        flag = 1
                        res_man += 1
                        break

            if flag == 0 and check_money:
                res_money += check_money

        res.append([res_man, res_money])

    def emo_check(idx, s):
        if len(s) == len(emoticons):
            check(s)
            return

        for i in range(idx, len(emoticons)):
            for dis in range(4):
                s.append([int(emoticons[i] * (100 - discount[dis]) / 100), discount[dis]])
                emo_check(i + 1, s)
                s.pop()

    emo_check(0, [])
    res.sort(key=lambda x: (-x[0], -x[1]))

    return res[0]