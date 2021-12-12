a, b = map(str, input().split())
c = d = ""
c += a[2] + a[1] + a[0]
d += b[2] + b[1] + b[0]
if c > d:
    print(c)
else:
    print(d)