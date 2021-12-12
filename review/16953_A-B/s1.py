import sys
sys.stdin = open('input.txt')
# sys.setrecursionlimit(10**6) # 	런타임 에러 (RecursionError)

def change(a, cnt):
    global result

    if a > B:
        return

    if cnt >= result:
        return

    if a == B:
        if result > cnt:
            result = cnt
        return

    change(a * 2, cnt + 1)
    change(a * 10 + 1, cnt + 1)

result = 1e9
A, B = map(int, input().split())
change(A, 1)
if result == 1e9:
    print(-1)
else:
    print(result)