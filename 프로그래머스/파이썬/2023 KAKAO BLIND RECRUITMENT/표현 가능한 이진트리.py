def solution(numbers):
    answer = []

    def check(i, s):
        if numbers[i] and (L := len(s) // 2):
            if s[L] == '0' and ('1' in s):
                numbers[i] = 0
            else:
                check(i, s[:L]), check(i, s[L + 1:])

    for i, n in enumerate(numbers):
        s, numbers[i] = bin(n)[2:], 1
        len_s, L = len(s), 1

        while len_s >= L:
            L *= 2
        # rjust L -1 의 크기만큰 '0'을 채워줌
        # s의길이가 3이고 L - 1가 7 이면 4개의 0을 왼쪽채워줌
        s = s.rjust(L - 1, '0')

        check(i, s)
    return numbers