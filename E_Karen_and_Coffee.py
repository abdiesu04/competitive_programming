s = "internationalization"
abbr = "i12iz4n"
n = len(s)
t = 0

for i in abbr:
    if i.isdigit():
        t = t * 10 + int(i)
    else:
        t += 1

print(t, n)
if t == n:
    print(True)
else:
    print(False)