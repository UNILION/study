import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
day = (V - B) // (A - B)
if (V - B) % (A - B) == 0:
    print(day)
else:
    print(day + 1)