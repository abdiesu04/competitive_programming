n, l, a = map(int, input().split())

nums = [0] * (l+1)

for _ in range(n):
    s, t = map(int, input().split())
    for i in range(s, s + t):
        nums[i] = 1

tmp = 0
cnt = 0

for i in range(len(nums)):
    if nums[i] == 0:
        tmp += 1
        if tmp == a:
            cnt += 1
            tmp = 0
    else:
        tmp = 0

if n == 0:
    print(a)
else:
    print(cnt)