t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    csum = 0
    ans = True
    for i, x in enumerate(a):
        csum += x
        if 2 * csum < i * (i + 1):
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")