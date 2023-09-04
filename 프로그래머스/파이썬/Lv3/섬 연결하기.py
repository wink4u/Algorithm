def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if a > b:
        parent[b] = a
    elif a < b:
        parent[a] = b

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    
    for i in range(len(costs)):
        s, e, cost = costs[i]
        
        if find(s, parent) != find(e, parent):
            answer += cost
            union(s, e, parent)
            
    return answer