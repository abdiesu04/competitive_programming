def solve():
    t = int(input())
    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        k = 0
        a.sort()
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                k += 1
        if k == 0:
            print(n)
        elif k % 2 == 0:
            print(n - k)
        else:
            print(n - k - 1)
        t -= 1

solve()