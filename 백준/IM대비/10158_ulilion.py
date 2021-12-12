"""
개미는 p + 1, q + 1로 움직임
가로가 세로보다 클 시
만약 오른쪽 경계에 다다르면 p-1 q + 1로 움직임
위쪽 경계에 다다르면 p-1 q-1로 움직임
아래쪽 경계에 다다르면 p-1 q+1
왼쪽 경계에 다다르면 p+1 q+1

세로가 가로보다 클 시
만약 오른쪽 경계에 다다르면 p-1 q + 1로 움직임
위쪽 경계에 다다르면 p-1 q-1로 움직임
왼쪽 경계에 다다르면 p+1 q-1
아래쪽 경계에 다다르면 p+1 q+1
"""
import sys
input = sys.stdin.readline
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
flag = 0
i = 0
turn = 0
# 0 = 우상, 1 = 우하, 2 = 좌상, 3 = 좌하
while i < t:
    if (flag == 0): # 우상
        if (p == w and q == h): # 좌하
            flag = 3
            turn = 1
        elif (p == w):          # 좌상
            flag = 2
            turn = 1
        elif (q == h):          # 우하
            flag = 1
            turn = 1
        else:
            p += 1
            q += 1
    
    elif (flag == 1):   # 우하
        if (p == w and q == 0): # 좌상
            flag = 2
            turn = 1
        elif (p == w):          # 좌하
            flag = 3
            turn = 1
        elif (q == 0):          # 우상
            flag = 0
            turn = 1
        else:
            p += 1
            q -= 1

    
    elif (flag == 2):   # 좌상
        if (p == 0 and q == h): # 우하
            flag = 1
            turn = 1
        elif (p == 0):          # 우상
            flag = 0
            turn = 1
        elif (q == h):          # 좌하
            flag = 3
            turn = 1
        else:
            p -= 1
            q += 1

    elif (flag == 3):   # 좌하 
        if (p == 0 and q == 0): # 우상
            flag = 0
            turn = 1
        elif (p == 0):          # 우하
            flag = 1
            turn = 1
        elif (q == 0):          # 좌상
            flag =2
            turn = 1
        else:
            p -= 1
            q -= 1

    if turn == 1:
        i -= 1
        turn = 0

    i += 1

print(p, q)