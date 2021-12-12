while True:
    string = input()
    if string[0] == '.':
        break
    stack = []
    flag = 0
    for x in string:
        if x == "(" or x == "[":
            stack.append(x)
        elif x == ")":
            if not stack:
                flag = 1
                break
            if stack.pop() != "(":
                flag = 1
                break
        elif x == "]":
            if not stack:
                flag = 1
                break
            if stack.pop() != "[":
                flag = 1
                break
    if flag or stack:
        print("no")
    else:
        print("yes")