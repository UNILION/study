"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys
input = sys.stdin.readline
N = int(input())
result = []
temp = []
for _ in range(N):
    init = list(input().split())
    if init[0] == "push_front":
        temp = result[:]
        result = []
        result.append(init[1])
        result[1:] = temp[:]
    elif init[0] == "push_back":
        result.append(init[1])

    elif init[0] == "pop_front":
        if result:
            print(result.pop(0))
        else:
            print(-1)
    elif init[0] == "pop_back":
        if result:
            print(result.pop())
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