N, X = map(int, input().split())
a = list(map(int, input().split()))
for idx in a:
    if idx < X:
        print(idx, end=" ")