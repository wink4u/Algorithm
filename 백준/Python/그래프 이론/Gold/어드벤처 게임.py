import sys
input = sys.stdin.readline

def dfs(now, money, t, v):
    global flag

    if type_list[now] == 'L':
        if money < cost[now]:
            money = cost[now]
    elif type_list[now] == 'T':
        if money < cost[now]:
            return
        else:
            money -= cost[now]

    if now == t:
        flag = 1
        return

    for n_node in node[now]:
        if not v[n_node]:
            v[n_node] = 1
            dfs(n_node, money, t, v)
            v[n_node] = 0

while True:
    n = int(input())
    # E는 빈방, L은 레프리콘, T는 트롤

    if n:
        flag = 0
        cost = [0]
        type_list = [0]
        node = [0]

        for _ in range(n):
            s = input().split()
            type_list.append(s[0])
            cost.append(int(s[1]))

            tmp = []
            for i in range(2, len(s) - 1):
                tmp.append(int(s[i]))

            node.append(tmp)

        visit = [0] * (n + 1)

        if type_list[1] == 'E' or type_list[1] == 'L':
            visit[1] = 1
            dfs(1, 0, n, visit)

        if flag:
            print('Yes')
        else:
            print('No')
    else:
        break