N = int(input())
N_list = [int(input()) for _ in range(N)]
temp = []
temp_list = []
result = []
cnt = 0
for i in range(1, N + 1):
    if i != N_list[cnt]:
        temp.append(i)
        result.append("+")
    else:
        temp.append(i)
        result.append("+")
        while temp and temp[-1] == N_list[cnt]:
            cnt += 1
            temp_list.append(temp.pop())
            result.append("-")

if temp_list == N_list:
    for r in result:
        print(r)
else:
    print("NO")