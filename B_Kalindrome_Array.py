t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    if len(set(nums)) == 1:
        print("YES")
        break
    stack1 = []
    stack2 = []
    l , r = 0, len(nums)-1
    while l <= r:
        if nums[l] != nums[r]:
            stack2.append(nums[r])
            r -= 1
        if nums[r] == nums[l]:
            l += 1
            r -= 1
    if len(stack2) <= 1:
        print('YES')
    else:
        print("NO")
            
    