class Solution:
    def compress(self, chars: List[str]) -> int:
        l, cnt = 0, 1
        for r in range(len(chars) - 1):
            if chars[r] == chars[r+1]:
                cnt += 1
            else:
                chars[l] = chars[r]
                if cnt > 1:
                    for digit in str(cnt):
                        l += 1
                        chars[l] = digit
                l += 1
                cnt = 1
        chars[l] = chars[-1]
        if cnt > 1:
            for digit in str(cnt):
                l += 1
                chars[l] = digit
        return len(chars[:l+1])