a, b = map(int, input().split())
result = 0
x = y = z = 1
for i in range(1, a + 1):
    x *= i
for j in range(1, b + 1):
    y *= j
for k in range(1, a - b + 1):
    z *= k
result = x//(y*z)
print(result)