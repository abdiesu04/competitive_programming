
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    p = True
    for i, x in enumerate(a):
        s += x
        if 2 * s < i * (i + 1):
            p = False
            break
    if p:
        print("YES")
    else:
        print("NO")