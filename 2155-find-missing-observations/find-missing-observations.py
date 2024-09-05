
class Solution:
    def missingRolls(self, rolls , mean: int, n: int):
        sum_of_rolls = sum(rolls)

        left_sums = (len(rolls) + n) * mean - sum_of_rolls

        if left_sums < n or left_sums > 6 * n:
            return []  # Return empty if not possible

        res = [1] * n 
        left_sums -= n
        i = 0
        while i < n and left_sums > 0:
            # Add as much as possible but not more than 5 (since max roll is 6)
           add = min(5, left_sums)
           res[i] += add
           left_sums -= add
           i += 1

        return res