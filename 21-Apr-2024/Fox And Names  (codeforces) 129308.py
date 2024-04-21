# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque

n = int(input())
word = input().strip()
graph = defaultdict(list)
incoming = defaultdict(int)

for _ in range(n - 1):
    line = input().strip()
    for w, l in zip(word, line):
        if w != l:
            graph[w].append(l)
            incoming[l] += 1
            break
    else:
        if len(line) < len(word):
            print('Impossible')
            exit()
    word = line

queue = deque()
ans = []
for i in range(26):
    if incoming[chr(ord('a') + i)] == 0:
        queue.append(chr(ord('a') + i))

while queue:
    node = queue.popleft()
    ans.append(node)
    for adj in graph[node]:
        incoming[adj] -= 1
        if incoming[adj] == 0:
            queue.append(adj)

if len(ans) != 26:
    print('Impossible')
else:
    print(''.join(ans))