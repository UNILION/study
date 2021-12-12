H, M = map(int, input().split())
if M - 45 < 0:
    M = 60 - (45 - M)
    if H >= 1:
        H -= 1
    else:
        H = 23
else:
    M -= 45
print(H, M)