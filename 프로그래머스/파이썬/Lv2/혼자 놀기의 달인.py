def solution(cards):
    answer = 0
    n = len(cards)
    visit = [0] * n

    ans = []
    for i in range(n):
        cnt = 0
        if not visit[i]:
            visit[i] = 1
            cnt += 1
            now = i
            while True:
                nxt = cards[now] - 1
                if not visit[nxt]:
                    visit[nxt] = 1
                    now = nxt
                    cnt += 1
                else:
                    break
            ans.append(cnt)

    ans.sort(reverse=True)

    if len(ans) == 1:
        return 0
    else:
        return ans[0] * ans[1]