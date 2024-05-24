class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Build the Trie
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # Find the maximum XOR
        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if node.children[1 - bit]:
                    curr_xor |= (1 << i)
                    node = node.children[1 - bit]
                else:
                    node = node.children[bit]
            max_xor = max(max_xor, curr_xor)

        return max_xor