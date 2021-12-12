a, b = map(int, input().split())
GCD = LCM = 0
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        GCD = i
print(GCD)
print((a * b) // GCD)