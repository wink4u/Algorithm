import heapq

def solution(ability, number):
    heapq.heapify(ability)

    for i in range(number):
        a, b = heapq.heappop(ability), heapq.heappop(ability)
        res = a + b

        heapq.heappush(ability, res)
        heapq.heappush(ability, res)

    return sum(ability)