# n, m = map(int, input().split())
# n_list = [list(map(str, input())) for _ in range (n)]
# result_list = []
# for i in range(n - 7):
#     for j in range(m - 7):
#         result = 0
#         for x in range(8):
#             for y in range(8):
#                 if (x + y) % 2 == 0:
#                     if n_list[i + x][j + y] != n_list[i][j]:
#                         result += 1
#                 else:
#                     if n_list[i + x][j + y] == n_list[i][j]:
#                         result += 1
#         result_list.append(result)
# print(min(result_list))


######### 구글링
n, m = map(int, input().split())
l = []
mini = []

for _ in range(n):
    l.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):
                if (j + b)%2 == 0:
                    if l[b][j] != 'W': idx1 += 1  
                    if l[b][j] != 'B': idx2 += 1
                else :
                    if l[b][j] != 'B': idx1 += 1
                    if l[b][j] != 'W': idx2 += 1
        mini.append(idx1)
        mini.append(idx2)

print(min(mini))