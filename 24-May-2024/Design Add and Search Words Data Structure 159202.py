# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            cur = node
            for i in range(i, len(word)):
                char = word[i]
                if char == '.':
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.end

        return dfs(self.root, 0)