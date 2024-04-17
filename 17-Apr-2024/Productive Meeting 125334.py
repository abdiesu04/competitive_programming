# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    sociability = list(map(int, input().split()))
    heap = []
    for i in range(n):
        if sociability[i] > 0:
            heapq.heappush(heap, (-sociability[i], i + 1))
    # print(heap)
    res = []
    while len(heap) > 1:
        p1 = heapq.heappop(heap)
        p2 = heapq.heappop(heap)
        # print(p1 , p2)
        res.append((p1[1], p2[1]))
        if abs(p1[0]) > 1:
            heapq.heappush(heap, (p1[0] + 1, p1[1]))
        if abs(p2[0]) > 1:
            heapq.heappush(heap, (p2[0] + 1, p2[1]))
    print(len(res))
    for p in res:
        print(p[0], p[1])