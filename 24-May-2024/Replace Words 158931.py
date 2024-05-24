# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True
        
    def search(self, word):
        cur = self.root
        res = ''
        for char in word:
            if char in cur.children:
                res += char
                cur = cur.children[char]
                if cur.isEnd:
                    break
            else:
                break
        return res if cur.isEnd else word
        
class Solution:
    def replaceWords(self, roots: List[str], sentence: str) -> str:
        t = Trie()
        for root in roots:
            t.insert(root)
        return ' '.join(t.search(word) for word in sentence.split())