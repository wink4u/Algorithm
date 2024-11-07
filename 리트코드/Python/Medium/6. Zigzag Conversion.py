class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        print(len(s))

        arr = [['' for _ in range(len(s))] for _ in range(numRows)]

        dx = [1, -1]
        dy = [0, 1]

        d = 0

        idx = 0
        x, y = 0, 0
        while idx < len(s):
            arr[x][y] = s[idx]

            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < numRows and 0 <= ny < len(s):
                x, y = nx, ny
            else:
                if d:
                    d = 0
                else:
                    d = 1

                x, y = x + dx[d], y + dy[d]

            idx += 1

        res = ''
        for i in range(len(arr)):
            res += ''.join(arr[i])

        return res