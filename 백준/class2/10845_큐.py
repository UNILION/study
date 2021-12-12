"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys
input = sys.stdin.readline
N = int(input())
result = []
for _ in range(N):
    init = list(input().split())
    if init[0] == "push":
        result.append(init[1])
    elif init[0] == "pop":
        if result:
            print(result.pop(0))
        else:
            print(-1)
    elif init[0] == "size":
        print(len(result))
    elif init[0] == "empty":
        if result:
            print(0)
        else:
            print(1)
    elif init[0] == "front":
        if result:
            print(result[0])
        else:
            print(-1)
    elif init[0] == "back":
        if result:
            print(result[-1])
        else:
            print(-1)