# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def inbound(i ,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        def backtrack(index , i , j ):
            if index  == len(word):
                return True
            if not inbound(i , j) or board[i][j] != word[index]:
                return False

            temp , board[i][j] = board[i][j] , "#"

            found = (backtrack(index + 1, i + 1 , j) or
                    backtrack(index + 1,i -1 , j) or 
                    backtrack(index + 1,i , j + 1) or 
                    backtrack(index + 1,i , j - 1))

            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(0 ,i , j):
                        return True

        return False