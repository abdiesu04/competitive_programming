# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())

def isPos(m, s):
    return s >= 0 and s <= 9 * m

mn = ""
rem = s
for i in range(m):
    for d in range(10):
        if (i > 0 or d > 0 or (m == 1 and d == 0)) and isPos(m - i - 1, rem - d):
            mn += str(d)
            rem -= d
            break

mx = ""
rem = s
for i in range(m):
    for d in range(9, -1, -1):
        if isPos(m - i - 1, rem - d):
            mx += str(d)
            rem -= d
            break

if len(mn) != m or len(mx) != m:
    print("-1 -1")
else:
    print(mn , mx)

