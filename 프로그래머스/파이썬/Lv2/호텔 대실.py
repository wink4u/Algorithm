import heapq


def solution(book_time):
    hotel = []

    book_time.sort(key=lambda x: (x[0], x[1]))
    s_h, s_m = book_time[0][1].split(':')
    heapq.heappush(hotel, int(s_h) * 60 + int(s_m))

    for i in range(1, len(book_time)):
        ns_h, ns_m = book_time[i][0].split(':')
        ne_h, ne_m = book_time[i][1].split(':')

        stime = int(ns_h) * 60 + int(ns_m)
        etime = int(ne_h) * 60 + int(ne_m) + 10

        if hotel[0] > stime:
            heapq.heappush(hotel, etime)
        else:
            heapq.heappop(hotel)
            heapq.heappush(hotel, etime)

    return len(hotel)