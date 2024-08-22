answer = 0

def solution(info, edges):
    n = len(info)
    node = [[] for _ in range(n)]

    for a, b in edges:
        node[a].append(b)

    def dfs(v, sheep, wolf, able):
        global answer

        if wolf >= sheep:
            return

        if sheep > answer:
            answer = sheep

        able.extend(node[v])

        for a in able:
            if info[a]:
                dfs(a, sheep, wolf + 1, [i for i in able if i != a])
            else:
                dfs(a, sheep + 1, wolf, [i for i in able if i != a])

    dfs(0, 1, 0, node[0])

    return answer