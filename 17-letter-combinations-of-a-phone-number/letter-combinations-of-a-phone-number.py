class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # step 1: map digits to characters
        chars = [digit_map[digit] for digit in digits]
        # step 2: obtain all possible combinations
        combs = product(*chars)  # or product(chrs for chrs in chars)
        result = []
        for comb in combs:
            if not comb:
                continue
            # step 3: concatenate characters
            string = ''.join(comb)
            # step 4: add to result list
            result.append(string)
        return result