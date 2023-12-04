nums = [34,23,1,24,75,33,54,8]
k = 60


def maxSum(nums, k):
    nums.sort()
    res = 0
    l , r = 0 , len(nums)- 1
    while l <= r:
        s = nums[l] + nums[r]
        if s <= k:
            res = max(res, s)
            l += 1
        if s >= k:
            r -= 1
    return res

print(maxSum(nums, k))


