t = int(input())
for _ in range(t):
    n_list = list(map(str, input()))
    stack = []
    flag = 1
    for n in n_list:
        if n == '(':
            stack.append(n)
        else:
            try:
                stack.pop()
            except:
                flag = 0
                break
    if stack or flag == 0:
        print("NO")
    else:
        print("YES")