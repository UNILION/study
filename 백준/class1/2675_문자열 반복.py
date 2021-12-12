t = int(input())
for _ in range(t):
    num, chr = input().split()
    for c in chr:
        print(c * int(num), end="")
    print()