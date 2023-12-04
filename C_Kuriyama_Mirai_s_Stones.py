n = int(input())
c = list(map(int,input().split()))
cu = [c[0]]
for i in range(1, n):
    cu.append(c[i] + cu[i-1])

c.sort()
cs = [c[0]]
for i in range(1, n):
    cs.append(c[i] + cs[i-1])

m = int(input())
a = []
for i in range(m):
    a.append(list(map(int,input().split())))

for i in a:
    t = i[0]
    b = i[1] - 1
    e = i[2] - 1
    if t == 1:
        if b == 0:
            print(cu[e])
        else:
            print(cu[e] - cu[b-1])
    else:
        if b == 0:
            print(cs[e])
        else:
            print(cs[e] - cs[b-1])