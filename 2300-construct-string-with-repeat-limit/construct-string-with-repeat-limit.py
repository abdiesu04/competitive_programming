class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt  = defaultdict(int)
        res  = []
        for letter in s:
            cnt[letter] += 1

        max_heap = []
        # for letter in s:
        #     heappush(max_heap , (-ord(letter) , cnt[letter]))
        for letter, count in cnt.items():
            heappush(max_heap, (-ord(letter), count))


        while max_heap:
            neg_ascii , count = heappop(max_heap)
            use  = min(repeatLimit  , count)
            res.append(chr(-neg_ascii)*use)

            if count > use and max_heap:
                next_chr , next_cnt = heappop(max_heap)
                res.append(chr(-next_chr))
                if next_cnt > 1:
                    heappush(max_heap , (next_chr , next_cnt  - 1))
                heappush(max_heap , (neg_ascii , count - use))

        return ''.join(res)




            