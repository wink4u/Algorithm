from collections import deque


def solution(x, y, n):
    def bfs():
        q = deque()
        q.append([y, 0])
        visit = [y]

        while q:
            now, cnt = q.popleft()

            if now == x:
                print(now, cnt)
                return cnt

            for i in range(3):
                if i == 0 and now % 2 == 0:
                    nxt = now // 2
                elif i == 1 and now % 3 == 0:
                    nxt = now // 3
                else:
                    nxt = now - n

                if nxt > 0 and nxt not in visit:
                    visit.append(nxt)
                    q.append([nxt, cnt + 1])

        return -1

    return bfs()
