def solve():
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()

    min_diff = float('inf')
    min_index = -1
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] < min_diff:
            min_diff = nums[i] - nums[i-1]
            min_index = i

    result = [nums[min_index-1]] + nums[min_index+1:] + nums[:min_index-1] + [nums[min_index]]
    print(' '.join(map(str, result)))

t = int(input())
for _ in range(t):
    solve()