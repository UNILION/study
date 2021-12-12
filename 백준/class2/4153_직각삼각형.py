while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    temp = [x, y, z]
    temp.sort()
    x, y, z = temp[0], temp[1], temp[2]
    if x ** 2 + y ** 2 == z ** 2:
        print("right")
    else:
        print("wrong")