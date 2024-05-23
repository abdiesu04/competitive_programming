class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def insert(self, root: TrieNode, word: str) -> None:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        root = TrieNode()
        for word in strs:
            self.insert(root, word)

        node = root
        prefix = ""
        while len(node.children) == 1 and not node.is_end:
            for char in node.children:
                node = node.children[char]
                prefix += char
        return prefix
