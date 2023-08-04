class Solution:
    def plusOne(self, digits: List[int]):

        return list(map(int, list(str(1+int("".join(list(map(str, digits))))))))