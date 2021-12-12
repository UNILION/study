T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    a, b = N % H, N // H + 1
    if a == 0:
        a, b = H, N // H
    print(a * 100 + b)