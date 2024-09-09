class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(index , comb , opening_cnt , closing_cnt):
            if index == 2 * n:
                res.append(comb)
                return

            if  closing_cnt < opening_cnt:
                backtrack(index + 1 , comb + ")", opening_cnt , closing_cnt + 1)
            if opening_cnt < n :
                backtrack(index + 1 , comb + "(", opening_cnt +1 , closing_cnt)

        backtrack(0 , '' , 0 , 0)
        return res
