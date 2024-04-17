# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq

n = int(input())
ans = []
heap = []

for _ in range(n):
    op = input().split()
    if op[0] == "insert":
        x = int(op[1])
        heapq.heappush(heap, x)
        ans.append((op[0], x))
    elif op[0] == "getMin":
        x = int(op[1])
        while heap and heap[0] < x:
            # print(heap)
            heapq.heappop(heap)
            ans.append(("removeMin", None))
        if not heap or heap[0] > x:
            # print(heap)
            heapq.heappush(heap, x)
            ans.append(("insert", x))
        ans.append((op[0], x))
    else: 
        if not heap:
            ans.append(("insert", 0))
        else:
            heapq.heappop(heap)
        ans.append((op[0], None))
# print(ans)
print(len(ans))
for op in ans:
    print(op[0], end=" ")
    if op[1] is not None:
        print(op[1])
    else:
        print()