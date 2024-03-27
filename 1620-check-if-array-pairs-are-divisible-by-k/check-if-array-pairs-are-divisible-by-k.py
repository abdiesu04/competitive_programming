class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter([arr[i] % k for i in range(len(arr))])
        if cnt[0] % 2!= 0:
            return False

        for i in range(1 , k-1):
            if cnt[i] != cnt[k-i]:
                return False
        return True