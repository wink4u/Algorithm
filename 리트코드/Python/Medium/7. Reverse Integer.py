class Solution:
    def reverse(self, x: int) -> int:
        x_s = str(x)

        if x_s[0] == '-':
            reverse = int('-' + x_s[:0:-1])
        else:
            reverse = int(x_s[::-1])

        if reverse < -(2 ** 31) or reverse > (2 ** 31) - 1:
            return 0

        return reverse