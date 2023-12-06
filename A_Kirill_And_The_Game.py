l, r, x, y, k = map(int, input().split())
ok = False
for i in range(x, y+1):
    if i*k >= l and i*k <= r:
        ok = True
if ok:
    print("YES")
else:
    print("NO")