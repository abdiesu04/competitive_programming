def is_palindrome(v):
    n = len(v)
    a = n // 2
    for i in range(a):
        if v[i] != v[n-i-1]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    if n == 2:
        print("YES")
        continue
    mp = {i: v.count(i) for i in v}
    a, b, c, d = [], [], [], []
    if v[0] != v[n-1]:
        if mp[v[0]] == 1 and mp[v[n-1]] == 1:
            print("NO")
            continue
        if mp[v[0]] > 1 or mp[v[n-1]] > 1:
            for i in range(n):
                if v[i] != v[0]:
                    a.append(v[i])
                if v[i] != v[n-1]:
                    b.append(v[i])
            if is_palindrome(a) or is_palindrome(b):
                print("YES")
            else:
                print("NO")
            continue
    else:
        flag = 0
        p, q = 0, 0
        i, j = 0, n-1
        while i < j:
            if v[i] == v[j]:
                i += 1
                j -= 1
            else:
                p = v[i]
                q = v[j]
                flag = 1
                break
        if flag == 0:
            print("YES")
            continue
        for i in range(n):
            if v[i] != p:
                c.append(v[i])
            if v[i] != q:
                d.append(v[i])
        if is_palindrome(c) or is_palindrome(d):
            print("YES")
        else:
            print("NO")
            continue