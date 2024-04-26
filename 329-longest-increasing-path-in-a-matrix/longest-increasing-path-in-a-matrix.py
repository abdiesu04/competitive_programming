class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(m):
            for j in range(n):
                for d in directions:
                    x = i + d[0]
                    y = j + d[1]
                    if m > x >= 0 and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        graph[(i, j)].append((x, y))
                        indegree[(x, y)] += 1

        que = deque([(i, j) for i in range(m) for j in range(n) if indegree[(i, j)] == 0])
        max_len = 0

        while que:
            level_size = len(que)

            for _ in range(level_size):
                i, j = que.popleft()
                
                for x, y in graph[(i, j)]:
                    indegree[(x, y)] -= 1
                    if indegree[(x, y)] == 0:
                        que.append((x, y))

            max_len += 1

        return max_len