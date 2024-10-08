class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * n
        candle_positions = []

        count = 0
        for i in range(n):
            if s[i] == '*':
                count += 1
            prefix[i] = count
            if s[i] == '|':
                candle_positions.append(i)

        def left_idx(num):
            left, right = 0, len(candle_positions)
            while left < right:
                mid = left + (right - left) // 2
                if candle_positions[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left

        def right_idx(num):
            left, right = 0, len(candle_positions)
            while left < right:
                mid = left + (right - left) // 2
                if candle_positions[mid] <= num:
                    left = mid + 1
                else:
                    right = mid
            return left

        res = []
        for start, end in queries:
            left = left_idx(start)
            right = right_idx(end) - 1

            if left < len(candle_positions) and right >= 0 and candle_positions[left] <= candle_positions[right]:
                first = candle_positions[left]
                second = candle_positions[right]
                res.append(prefix[second] - prefix[first])
            else:
                res.append(0)

        return res
