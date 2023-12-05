# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# s = list(input())
# ans = 0
# if n == k:
#     print(sum(a))
# else:
#     i = 0
#     while i < n:
#         j = i + 1
#         ss = [a[i]]
#         while j < n and s[i] == s[j]:
#             ss.append(a[j])
#             j += 1
#         ss.sort()
#         m = sum(ss[-k:])
#         ans += m
#         i = j
#     print(ans)



l = 'abdbsrw'
def checkUniqueness(a):
    return len(set(a)) == len(a)
l , r  = 0 , len(l) - 1
ans = 0
while l < r:
    if checkUniqueness(l[l:r+1]):
        ans = max(ans , r - l + 1)
    

