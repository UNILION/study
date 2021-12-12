a, b, c, d, e, f, g, h = input().split()
if a < b < c < d < e < f < g < h:
    print("ascending")
elif h < g < f < e < d < c < b < a:
    print("descending")
else:
    print("mixed")