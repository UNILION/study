a, b = map(int, input().split())
visited = [0] * (a + 1)
n_list = []
flag = 1
while visited.count(0) != 1:
    for i in range(1, a + 1):
        if not visited[i]:
            if flag == b:
                visited[i] = 1
                flag = 1
                n_list.append(i)
            else:
                flag += 1
print("<", end="")
for j in n_list:
    if j != n_list[-1]:
        print(j, end=", ")
    else:
        print(j, end=">")