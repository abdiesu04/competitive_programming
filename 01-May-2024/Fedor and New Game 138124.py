# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n , m , k = map(int,input().split())
arr  = []
for _ in range(m+1):
    n = int(input())
    # print(bin(n))
    arr.append(n)
m = arr[-1]
cnt = 0
for i in range(len(arr)-1):
    if bin(arr[i] ^ m).count("1") <= k:
        cnt += 1
print(cnt)
    