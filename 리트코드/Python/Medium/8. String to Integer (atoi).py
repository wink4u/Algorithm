class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)

        # print(ord('3'))
        res = ''
        flag = False
        minus = False
        for i in s:
            if len(res):
                if 48 <= ord(i) <= 57:
                    res += i
                else:
                    break
            else:
                if ord(i) == 43:
                    if flag:
                        break
                    flag = True
                    continue
                elif ord(i) == 45:
                    if flag:
                        break
                    flag = True
                    minus = True
                elif 48 <= ord(i) <= 57:
                    res += i
                else:
                    break

        if len(res):
            if minus:
                res = '-' + res

            if int(res) < -(2 ** 31):
                return -(2 ** 31)
            elif int(res) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return int(res)

        else:
            return 0