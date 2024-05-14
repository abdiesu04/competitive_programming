# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        leaves = deque()
        for node in adj_list:
            if len(adj_list[node]) == 1:
                leaves.append(node)

        rem = n
        while rem > 2:
            num_leaves = len(leaves)
            rem -= num_leaves

            for _ in range(num_leaves):
                leaf = leaves.popleft()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)

                if len(adj_list[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)